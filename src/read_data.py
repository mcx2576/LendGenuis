import os

import pandas as pd

# get the current working directory
current_working_directory = os.getcwd()

# Get the list of all files and directories
path = f"{current_working_directory}/data"
dir_list = os.listdir(path)

df = pd.read_excel(f"{current_working_directory}/data/{dir_list[0]}").iloc[:, -2:]
df.columns = ["item_1_short", "Labelling"]
for file in dir_list[1:]:
    next_df = pd.read_excel(f"{current_working_directory}/data/{file}").iloc[:, -2:]
    next_df.columns = ["item_1_short", "Labelling"]
    df = pd.concat([df, next_df])
