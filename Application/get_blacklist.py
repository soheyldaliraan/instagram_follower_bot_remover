import os
import pandas as pd

import configuration


def get_blacklist():
    if os.path.exists(configuration.blacklist_path):
        black_list = pd.read_csv(configuration.blacklist_path)
        return list(black_list['pk'])
    return []

