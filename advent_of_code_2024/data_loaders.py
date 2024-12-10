import pathlib
import re
from collections.abc import Sequence

import pandas as pd

from .data_structures import Report, ReportWithDampener
from .utility import as_int


def read_csv(filename: str) -> pd.DataFrame:
    input_path = pathlib.Path("data") / filename
    return pd.read_csv(input_path, delimiter=";", header=None)


def load_reports(filename: str) -> Sequence[Report]:
    input_path = pathlib.Path("data") / filename
    with open(input_path) as f_input:
        data = [
            Report([int(x.strip()) for x in row.split(" ")])
            for row in f_input.readlines()
        ]
    return data


def load_reports_with_dampener(filename: str) -> Sequence[ReportWithDampener]:
    input_path = pathlib.Path("data") / filename
    with open(input_path) as f_input:
        data = [
            ReportWithDampener([int(x.strip()) for x in row.split(" ")])
            for row in f_input.readlines()
        ]
    return data


def load_memory_string(memory: str) -> Sequence[tuple[int, int]]:
    input_path = pathlib.Path("data") / memory
    with open(input_path) as f_input:
        data = f_input.read().replace("\n", "")
    matches: list[str] = re.findall(r"mul\(\d+,\d+\)", data)
    values = [[as_int(num) for num in match.split(",")] for match in matches]
    return [(value[0], value[1]) for value in values]
