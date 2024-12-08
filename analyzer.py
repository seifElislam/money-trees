"""

"""
from time import time
import pandas as pd
import numpy as np
import swifter

from street_trees import StreetTreeType


class StatsAnalyzer:
    """

    """

    def __init__(self, street_trees_types):
        """

        """
        self.final_df = pd.DataFrame()
        self.street_trees_dataset = street_trees_types

    def analyze(self, dataset_csv_path, chuck_size):
        """

        :param dataset_csv_path:
        :param chuck_size:
        :return:
        """
        for chunk in pd.read_csv(dataset_csv_path, chunksize=chuck_size, encoding="windows-1252"):
            partial_result = self.__process_chuck(chunk)
            self.final_df = pd.concat([self.final_df, partial_result], ignore_index=True)

    def __process_chuck(self, chunck):
        """
        clean cost, add columns is_tall_street, is_short_street
        :param chuck:
        :return:
        """
        # clean price
        chunck['Price'] = chunck.Price.replace({'€': '', ',': ''}, regex=True).astype(float)
        check_type_vectorized = np.vectorize(self.street_trees_dataset.get_street_type)
        # chunck['type'] = chunck['Street Name'].apply(self.street_trees_dataset.get_street_type)
        chunck['type'] = check_type_vectorized(chunck['Street Name'])
        # chunck['type'] = chunck['Street Name'].swifter.apply(lambda row: street_trees_dataset.get_street_type(row))
        return chunck

    def stats(self):
        """

        :return:
        """
        avg_cost_short_streets = self.final_df.loc[self.final_df["type"] == 'short', "Price"].mean()
        avg_cost_tall_streets = self.final_df.loc[self.final_df["type"] == 'tall', "Price"].mean()
        return {'avg of cost of short streets': float(avg_cost_short_streets),
                'avg of cost of tall streets': float(avg_cost_tall_streets)}


if __name__ == '__main__':
    start = time()
    path = 'dublin-property.csv'
    dataset_path = 'dublin-trees.json'
    street_trees_dataset = StreetTreeType(dataset_path)
    analyzer = StatsAnalyzer(street_trees_dataset)
    analyzer.analyze(path, 10000)
    print(analyzer.stats())
    print(time() - start)
