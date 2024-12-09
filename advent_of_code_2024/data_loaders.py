import pathlib

import pandas as pd


def read_csv(csv_name: str) -> pd.DataFrame:
    input_path = pathlib.Path("data") / csv_name
    return pd.read_csv(input_path, delimiter=";", header=None)
