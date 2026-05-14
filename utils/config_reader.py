import json


def read_config():

    with open("config/config.json") as config_file:

        config = json.load(config_file)

    return config
