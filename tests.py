"""

"""
import unittest
from unittest.mock import MagicMock, patch
from analyzer import StatsAnalyzer
from street_trees import StreetTreeType


class TestAnalyzer(unittest.TestCase):
    """

    """

    def setUp(self):
        """

        :return:
        """
        mock_street_trees_dataset = MagicMock()
        self.analyzer = StatsAnalyzer(mock_street_trees_dataset)

    def test_clean_price(self):
        """

        :return:
        """
        values = ['€ 140,000.00', '140,000.00 $', '140,000']
        clean_values = ['140000.00', '140000.00', '140000']
        for value, clean_value in zip(values, clean_values):
            assert clean_value == self.analyzer.clean_currency(value)


class TestStreetTrees(unittest.TestCase):
    """

    """

    def test_short_tall_logic(self):
        """

        :return:
        """
        with patch('street_trees.StreetTreeType.load_dataset') as load_dummy_dataset:
            load_dummy_dataset.return_value = {"short": {"park": {
                "annesley": {
                    "annesley park": 10
                }}}, "tall": {"road": {
                "adelaide": {
                    "adelaide road": 25
                }, }}}
            street_trees_dataset = StreetTreeType('file.json')
            assert street_trees_dataset.get_street_type('annesley park') == 'short'
            assert street_trees_dataset.get_street_type('adelaide road') == 'tall'
