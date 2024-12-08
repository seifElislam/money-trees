import json
import csv
from time import time

import dpath

PROPERTY_CSV = 'dublin-property.csv'
STREET_TREES = 'dublin-trees.json'


def is_short(data, path):
    try:
        if dpath.get(data['short'], path):
            return True
    except KeyError:
        return False


def is_tall(data, path):
    try:
        if dpath.get(data['tall'], path):
            return True
    except KeyError:
        return False


def get_street_trees_type(street_trees, street_name_path):
    return {'short': is_short(street_trees, street_name_path), 'tall': is_tall(street_trees, street_name_path)}


if __name__ == '__main__':
    start = time()
    with open(STREET_TREES) as fh:
        street_trees_data = json.load(fh)
    with open(PROPERTY_CSV, 'r', encoding='iso-8859-1') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        count = 0
        for row in csv_reader:
            parts = row['Street Name'].strip().split(' ')
            path = '/'.join(parts[-1::-1])
            print(row['Street Name'].strip(), path)
            get_street_trees_type(street_trees_data, path.strip())
            count += 1
    print(time() - start)
    print(count)

