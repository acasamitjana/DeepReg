import os

# this is the path to the config file that is to be used
path_to_config_file = r'/home/ssd/Desktop/DeepReg_Project/insp_to_exp_config.yaml'

# takes approximately 4-5 minutes to generate tfrecords file
os.system('deepreg_gen_tfrecord' + ' -c ' + path_to_config_file)

print('Created the TFRECORD files!')

# refer to teh DeepReg github to see what options to use
os.system('deepreg_train' + ' -g \"\" ' + ' -c ' + path_to_config_file + ' --log insp_to_exp_log_train')
