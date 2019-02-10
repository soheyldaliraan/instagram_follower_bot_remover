import os
import pandas as pd

import configuration


def get_whitelist():
    if os.path.exists(configuration.whitelist_path):
        whitelist = pd.read_csv(configuration.whitelist_path)
        return list(whitelist['pk'])
    return []
