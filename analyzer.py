"""
Main program file to analyze the data set files
"""
import pandas as pd
import numpy as np
from cleantext import clean

from validator import check_input_files
from street_trees import StreetTreeType
from config import ENCODING, COLUMNS, BATCH_SIZE
from custom_exceptions import NonValidColumnsException, AppException
from logs import log_exceptions
from config import ENV


class StatsAnalyzer:
    """
    Analyzer class that process data set files and return mean stats of properties cost
    """

    def __init__(self, street_trees_types):
        """
        init class function
        """
        self.final_df = pd.DataFrame()
        self.street_trees_dataset = street_trees_types
        self.valid_columns = False

    @log_exceptions
    def process(self, dataset_csv_path, chuck_size):
        """
        load and process data set csv file
        :param dataset_csv_path: data set csv file path
        :param chuck_size: chuck size when processing the data set
        :return: final dataframe
        """
        for chunk in pd.read_csv(dataset_csv_path, chunksize=chuck_size, encoding=ENCODING, on_bad_lines='warn'):
            partial_result = self.__process_chuck(chunk)
            self.final_df = pd.concat([self.final_df, partial_result], ignore_index=True)

    def __process_chuck(self, chunk):
        """
        clean cost, add columns is_tall_street, is_short_street
        :param chuck: dataframe chunk
        :return: processed chunk
        """
        if not self.valid_columns:
            self.__check_columns(chunk)
        chunk = chunk.dropna()
        chunk = self.__clean_price_column(chunk)
        chunk = self.__update_df_with_street_tree_type(chunk)
        return chunk

    def __check_columns(self, chunk):
        """
        validate data set columns names
        :param chunk:
        :return: None
        """
        status = [c in chunk.columns for c in COLUMNS.split(',')]
        if all(status):
            self.valid_columns = True
            return
        raise NonValidColumnsException

    def __clean_price_column(self, df):
        """
        clean data set Price column from currency symbols
        :param df: input dataframe
        :return: cleaned "Price" column in the dataframe
        """
        # df['Price'] = df.Price.replace({'€': '', ',': ''}, regex=True).astype(float)
        clean_currency_vectorized = np.vectorize(self.clean_currency)
        df['Price'] = clean_currency_vectorized(df['Price']).astype(float)
        return df

    @staticmethod
    def clean_currency(value):
        """ If the value is a string, then remove currency symbol and delimiters
        otherwise, the value is numeric and can be converted
        """
        return clean(value, no_currency_symbols=True, replace_with_currency_symbol="").replace(',', '')

    def __update_df_with_street_tree_type(self, df):
        """
        check street trees type and add column "type" in the dataframe
        :param df: input dataframe
        :return: processed dataframe with 'type' column
        """
        check_type_vectorized = np.vectorize(self.street_trees_dataset.get_street_type)
        df['type'] = check_type_vectorized(df['Street Name'])
        return df

    @log_exceptions
    def stats(self):
        """
        return mean property cost analysis
        :return: json object contains the mean cost analysis
        """
        avg_cost_short_streets = self.final_df.loc[self.final_df["type"] == 'short', "Price"].mean()
        avg_cost_tall_streets = self.final_df.loc[self.final_df["type"] == 'tall', "Price"].mean()
        return {'avg_cost_of_property_on_short_trees_street': float(avg_cost_short_streets),
                'avg_cost_of_property_on_tall_trees_street': float(avg_cost_tall_streets)}


if __name__ == '__main__':
    path = 'data/dublin-property.csv'
    dataset_path = 'data/dublin-trees.json'
    try:
        check_input_files([path, dataset_path])
        street_trees_dataset = StreetTreeType(dataset_path)
        analyzer = StatsAnalyzer(street_trees_dataset)
        analyzer.process(path, BATCH_SIZE)
        print(analyzer.stats())
    except AppException as e:
        print({"error": "An unexpected error occurred. Please try again later." if ENV == "production" else str(e)})

