import pathlib

import numpy as np
import numpy.typing as npt
import pandas as pd


def load_csv_as_df(filename: str, delimiter: str = ";") -> pd.DataFrame:
    input_path = pathlib.Path("data") / filename
    return pd.read_csv(input_path, delimiter=delimiter, header=None)


def load_file_as_array(filename: str) -> npt.NDArray[np.str_]:
    lines = load_file_as_lines(filename)
    return np.array([list(line.strip()) for line in lines])


def load_file_as_blocks(filename: str) -> list[str]:
    input_path = pathlib.Path("data") / filename
    with open(input_path) as f_input:
        data = f_input.read()
    return data.split("\n\n")


def load_file_as_lines(filename: str) -> list[str]:
    input_path = pathlib.Path("data") / filename
    with open(input_path) as f_input:
        lines = f_input.readlines()
    return lines


def load_file_as_string(filename: str) -> str:
    input_path = pathlib.Path("data") / filename
    with open(input_path) as f_input:
        data = f_input.read().replace("\n", "")
    return data
