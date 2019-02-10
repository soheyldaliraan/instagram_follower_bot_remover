import os
import pandas as pd

import configuration


def remove_from_blacklist(pk):
    if os.path.exists(configuration.blacklist_path):
        black_dataset = pd.read_csv(configuration.blacklist_path)

        black_dataset.drop(black_dataset[black_dataset['pk'] == pk].index, inplace=True)

        black_dataset.to_csv(configuration.blacklist_path, columns=['pk', 'username'])
