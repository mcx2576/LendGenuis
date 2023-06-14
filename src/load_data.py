import os

import pandas as pd
from dotenv import dotenv_values


def read_env(path_file):
    """Read the .env file keys."""
    return dotenv_values(path_file + "/.env")


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
