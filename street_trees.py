"""

"""
import json
import dpath


class StreetTreeType:
    """

    """

    def __init__(self, dataset_file_path):
        """

        :param dataset_file_path:
        """
        self.dataset = self.load_dataset(dataset_file_path)

    @staticmethod
    def load_dataset(file_path):
        """

        :param file_path:
        :return:
        """
        with open(file_path) as fh:
            content = json.load(fh)
        return content

    def __is_short(self, path):
        """

        :param path:
        :return:
        """
        try:
            if dpath.get(self.dataset['short'], path):
                return True
        except KeyError:
            return False

    def __is_tall(self, path):
        """

        :param path:
        :return:
        """
        try:
            if dpath.get(self.dataset['tall'], path):
                return True
        except KeyError:
            return False

    def get_street_type(self, street_name):
        """

        :param street_name:
        :return:
        """
        parts = street_name.strip().split(' ')
        path = '/'.join(parts[-1::-1])
        if self.__is_short(path):
            return 'short'
        elif self.__is_tall(path):
            return 'tall'
        return 'n/a'
