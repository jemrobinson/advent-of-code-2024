import pathlib

import pandas as pd

from .data_structures import Report


def read_csv(filename: str) -> pd.DataFrame:
    input_path = pathlib.Path("data") / filename
    return pd.read_csv(input_path, delimiter=";", header=None)


def load_reports(filename: str) -> list[Report]:
    input_path = pathlib.Path("data") / filename
    with open(input_path) as f_input:
        data = [
            Report([int(x.strip()) for x in row.split(" ")])
            for row in f_input.readlines()
        ]
    return data
