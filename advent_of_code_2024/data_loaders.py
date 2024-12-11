import pathlib
from collections.abc import Sequence

import pandas as pd

from .report import Report, ReportWithDampener


def load_csv_as_df(filename: str, delimiter: str = ";") -> pd.DataFrame:
    input_path = pathlib.Path("data") / filename
    return pd.read_csv(input_path, delimiter=delimiter, header=None)


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


def load_print_queue_rules(filename: str) -> Sequence[tuple[int, int]]:
    return [
        (int(row[0]), int(row[1]))
        for _, row in load_csv_as_df(filename, delimiter="|").iterrows()
    ]


def load_print_queue_updates(filename: str) -> Sequence[Sequence[int]]:
    return [list(map(int, line.split(","))) for line in load_file_as_lines(filename)]


def load_reports(filename: str) -> Sequence[Report]:
    return [
        Report([int(x.strip()) for x in line.split(" ")])
        for line in load_file_as_lines(filename)
    ]


def load_reports_with_dampener(filename: str) -> Sequence[ReportWithDampener]:
    return [
        ReportWithDampener([int(x.strip()) for x in line.split(" ")])
        for line in load_file_as_lines(filename)
    ]
