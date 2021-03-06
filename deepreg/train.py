"""
Module to train a network using init files and a CLI
"""

import argparse
import logging
import os
from datetime import datetime

import tensorflow as tf

import deepreg.config.parser as config_parser
import deepreg.model.optimizer as opt
from deepreg.dataset.load import get_data_loader
from deepreg.model.network.build import build_model


def init(config_path, log_dir, ckpt_path):
    """
    Function to initialise log directories,
    assert that checkpointed model is the right
    type and to parse the configuration for training
    :param config_path: list of str, path to config file
    :param log_dir: str, path to where training logs
                    to be stored.
    :param ckpt_path: str, path where model is stored.
    """

    # init log directory
    log_dir = os.path.join(
        "logs", datetime.now().strftime("%Y%m%d-%H%M%S") if log_dir == "" else log_dir
    )
    if os.path.exists(log_dir):
        logging.warning("Log directory {} exists already.".format(log_dir))
    else:
        os.makedirs(log_dir)

    # check checkpoint path
    if ckpt_path != "":
        if not ckpt_path.endswith(".ckpt"):
            raise ValueError("checkpoint path should end with .ckpt")

    # load and backup config
    config = config_parser.load_configs(config_path)
    config_parser.save(config=config, out_dir=log_dir)
    return config, log_dir


def train(
    gpu: str, config_path: list, gpu_allow_growth: bool, ckpt_path: str, log_dir: str
):
    """
    Function to train a model
    :param gpu: str, which local gpu to use to train
    :param config_path: str, path to configuration set up
    :param gpu_allow_growth: bool, whether or not to allocate
                             whole GPU memory to training
    :param ckpt_path: str, where to store training ckpts
    :param log_dir: str, where to store logs in training
    """
    # env vars
    os.environ["CUDA_VISIBLE_DEVICES"] = gpu
    os.environ["TF_FORCE_GPU_ALLOW_GROWTH"] = "true" if gpu_allow_growth else "false"

    # load config
    config, log_dir = init(config_path, log_dir, ckpt_path)
    dataset_config = config["dataset"]
    preprocess_config = config["train"]["preprocess"]
    optimizer_config = config["train"]["optimizer"]
    model_config = config["train"]["model"]
    loss_config = config["train"]["loss"]
    num_epochs = config["train"]["epochs"]
    save_period = config["train"]["save_period"]
    histogram_freq = save_period

    # data
    data_loader_train = get_data_loader(dataset_config, "train")
    if data_loader_train is None:
        raise ValueError(
            "Training data loader is None. Probably the data dir path is not defined."
        )
    data_loader_val = get_data_loader(dataset_config, "valid")
    dataset_train = data_loader_train.get_dataset_and_preprocess(
        training=True, repeat=True, **preprocess_config
    )
    dataset_val = (
        data_loader_val.get_dataset_and_preprocess(
            training=False, repeat=True, **preprocess_config
        )
        if data_loader_val is not None
        else None
    )
    dataset_size_train = data_loader_train.num_samples
    dataset_size_val = (
        data_loader_val.num_samples if data_loader_val is not None else None
    )
    steps_per_epoch_train = max(
        dataset_size_train // preprocess_config["batch_size"], 1
    )
    steps_per_epoch_valid = (
        max(dataset_size_val // preprocess_config["batch_size"], 1)
        if data_loader_val is not None
        else None
    )

    strategy = tf.distribute.MirroredStrategy()
    with strategy.scope():
        # model
        model = build_model(
            moving_image_size=data_loader_train.moving_image_shape,
            fixed_image_size=data_loader_train.fixed_image_shape,
            index_size=data_loader_train.num_indices,
            labeled=dataset_config["labeled"],
            batch_size=preprocess_config["batch_size"],
            model_config=model_config,
            loss_config=loss_config,
        )

        # compile
        optimizer = opt.get_optimizer(optimizer_config)

        model.compile(optimizer=optimizer)

        # load weights
        if ckpt_path != "":
            model.load_weights(ckpt_path)

        # train
        # callbacks
        tensorboard_callback = tf.keras.callbacks.TensorBoard(
            log_dir=log_dir, histogram_freq=histogram_freq
        )
        checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=log_dir + "/save/weights-epoch{epoch:d}.ckpt",
            save_weights_only=True,
            period=save_period,
        )
        # it's necessary to define the steps_per_epoch and validation_steps to prevent errors like
        # BaseCollectiveExecutor::StartAbort Out of range: End of sequence
        model.fit(
            x=dataset_train,
            steps_per_epoch=steps_per_epoch_train,
            epochs=num_epochs,
            validation_data=dataset_val,
            validation_steps=steps_per_epoch_valid,
            callbacks=[tensorboard_callback, checkpoint_callback],
        )

    data_loader_train.close()
    if data_loader_val is not None:
        data_loader_val.close()


def main(args=None):
    """Entry point for train script"""

    parser = argparse.ArgumentParser(
        description="train", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    ## ADD POSITIONAL ARGUMENTS
    parser.add_argument(
        "--gpu",
        "-g",
        help="GPU index for training."
        '-g "" for using CPU'
        '-g "0" for using GPU 0'
        '-g "0,1" for using GPU 0 and 1.',
        type=str,
        required=True,
    )

    parser.add_argument(
        "--gpu_allow_growth",
        "-gr",
        help="Prevent TensorFlow from reserving all available GPU memory",
        default=False,
    )

    parser.add_argument(
        "--ckpt_path",
        "-k",
        help="Path of the saved model checkpoint to load."
        "No need to provide if start training from scratch.",
        default="",
        type=str,
        required=False,
    )

    parser.add_argument(
        "--log_dir",
        "-l",
        help="Name of log directory. The directory is under logs/."
        "If not provided, a timestamp based folder will be created.",
        default="",
        type=str,
    )

    parser.add_argument(
        "--config_path",
        "-c",
        help="Path of config, must end with .yaml. Can pass multiple paths.",
        type=str,
        nargs="+",
        required=True,
    )

    args = parser.parse_args(args)
    train(
        args.gpu, args.config_path, args.gpu_allow_growth, args.ckpt_path, args.log_dir
    )


if __name__ == "__main__":
    main()
