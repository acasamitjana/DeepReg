"""
Loads unpaired data
supports h5 and nifti formats
supports labeled and unlabeled data
"""
import random

from deepreg.dataset.loader.interface import (
    AbstractUnpairedDataLoader,
    GeneratorDataLoader,
)
from deepreg.dataset.util import check_difference_between_two_lists


class UnpairedDataLoader(AbstractUnpairedDataLoader, GeneratorDataLoader):
    """
    Loads unpaired data using given file loader, handles both labeled
    and unlabeled cases
    The function sample_index_generator needs to be defined for the
    GeneratorDataLoader class
    """

    def __init__(
        self,
        file_loader,
        data_dir_path: str,
        labeled: bool,
        sample_label: str,
        seed,
        image_shape: (list, tuple),
    ):
        """
        Load data which are unpaired, labeled or unlabeled

        :param file_loader:
        :param data_dir_path: path of the directory storing data,  the data has to be saved under four different
                              sub-directories: images, labels
        :param sample_label:
        :param seed:
        :param image_shape: (width, height, depth)
        """
        super(UnpairedDataLoader, self).__init__(
            image_shape=image_shape,
            labeled=labeled,
            sample_label=sample_label,
            seed=seed,
        )
        loader_image = file_loader(dir_path=data_dir_path, name="images", grouped=False)
        self.loader_moving_image = loader_image
        self.loader_fixed_image = loader_image
        if self.labeled:
            loader_label = file_loader(
                dir_path=data_dir_path, name="labels", grouped=False
            )
            self.loader_moving_label = loader_label
            self.loader_fixed_label = loader_label
        self.validate_data_files()

        self.num_images = self.loader_moving_image.get_num_images()
        self._num_samples = self.num_images // 2

    def validate_data_files(self):
        """Verify all loader have the same files"""
        if self.labeled:
            image_ids = self.loader_moving_image.get_data_ids()
            label_ids = self.loader_moving_label.get_data_ids()
            check_difference_between_two_lists(list1=image_ids, list2=label_ids)

    def sample_index_generator(self):
        """
        generates smaple indexes in orer to laod data using the
        GeneratorDataLoader class
        """
        image_indices = [i for i in range(self.num_images)]
        random.Random(self.seed).shuffle(image_indices)
        for sample_index in range(self.num_samples):
            moving_index, fixed_index = 2 * sample_index, 2 * sample_index + 1
            yield moving_index, fixed_index, [moving_index, fixed_index]

    def close(self):
        self.loader_moving_image.close()
        if self.labeled:
            self.loader_moving_label.close()
