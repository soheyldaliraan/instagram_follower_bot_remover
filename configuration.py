import os
import json

configuration_path = os.path.dirname(os.path.realpath(__file__))+"/configuration.json"
with open(configuration_path) as f:
    configuration_dict = json.load(f)

data_directory_path = os.path.dirname(os.path.realpath(__file__))+"/Data"

username = configuration_dict['username']
password = configuration_dict['password']

whitelist_path = configuration_dict['whitelist_path'] if configuration_dict['whitelist_path'] != "" else data_directory_path+"/WhiteList.csv"
blacklist_path = configuration_dict['blacklist_path'] if configuration_dict['blacklist_path'] != "" else data_directory_path+"/BlackList.csv"
