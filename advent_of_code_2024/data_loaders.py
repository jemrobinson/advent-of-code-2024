import pathlib

import pandas as pd


def read_csv(csv_name: str) -> pd.DataFrame:
    input_path = pathlib.Path("data") / csv_name
    return pd.read_csv(input_path, delimiter=";", header=None)


def df_distance(df: pd.DataFrame) -> int:
    loc_ids_0 = df.iloc[:, 0].sort_values().reset_index(drop=True)
    loc_ids_1 = df.iloc[:, 1].sort_values().reset_index(drop=True)
    return sum(abs(loc_ids_1 - loc_ids_0))
