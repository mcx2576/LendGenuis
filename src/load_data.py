import os

import pandas as pd


def read_env(path_file):
    """Read the .env file keys."""
    env = {}

    for line in open(path_file + "/.env", "r"):
        key_value = line.split("=")
        env[key_value[0].strip()] = key_value[1].strip()

    return env


def read_data(path_file):
    """Read the data

    Returns:
        df: return merged df
    """
    # Get the list of all files and directories
    dir_list = os.listdir(path_file)

    df = pd.read_excel(f"{path_file}/{dir_list[0]}").iloc[:, -2:]
    df.columns = ["item_1_short", "Labelling"]
    for file in dir_list[1:]:
        next_df = pd.read_excel(f"{path_file}/{file}").iloc[:, -2:]
        next_df.columns = ["item_1_short", "Labelling"]
        df = pd.concat([df, next_df])

    return df
