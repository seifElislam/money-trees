"""
Street trees type checker module
"""
import json
import dpath


class StreetTreeType:
    """
    Check street tree type using a street name
    """

    def __init__(self, dataset_file_path):
        """
        init class method
        :param dataset_file_path: street trees json file
        """
        self.dataset = self.load_dataset(dataset_file_path)

    @staticmethod
    def load_dataset(file_path):
        """
        read data set json file
        :param file_path:
        :return: file content
        """
        with open(file_path) as fh:
            content = json.load(fh)
        return content

    def __is_short(self, path):
        """
        check if trees in street are short
        :param path: modified street name to check it in the dataset
        :return: Boolean
        """
        try:
            if dpath.get(self.dataset['short'], path):
                return True
        except KeyError:
            return False

    def __is_tall(self, path):
        """
        check if trees in street are tall
        :param path: modified street name to check it in the dataset
        :return: Boolean
        """
        try:
            if dpath.get(self.dataset['tall'], path):
                return True
        except KeyError:
            return False

    def get_street_type(self, street_name):
        """
        return street trees type by street name.
        :param street_name:
        :return: street trees type, values are "short", "tall" or "n/a"
        """
        parts = street_name.strip().split(' ')
        path = '/'.join(parts[-1::-1])
        if self.__is_short(path):
            return 'short'
        elif self.__is_tall(path):
            return 'tall'
        return 'n/a'
