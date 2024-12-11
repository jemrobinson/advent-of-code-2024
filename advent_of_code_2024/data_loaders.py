import pathlib
from collections.abc import Sequence

import pandas as pd

from .data_structures import Report, ReportWithDampener, WordSearch, WordSearchSimple


def read_csv(filename: str) -> pd.DataFrame:
    input_path = pathlib.Path("data") / filename
    return pd.read_csv(input_path, delimiter=";", header=None)


def load_print_queue_rules(filename: str) -> Sequence[tuple[int, int]]:
    input_path = pathlib.Path("data") / filename
    return [
        (int(row[0]), int(row[1]))
        for _, row in pd.read_csv(input_path, delimiter="|", header=None).iterrows()
    ]


def load_print_queue_updates(filename: str) -> Sequence[Sequence[int]]:
    input_path = pathlib.Path("data") / filename
    updates = []
    with open(input_path) as f_input:
        for line in f_input.readlines():
            updates.append(list(map(int, line.split(","))))
    return updates


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


def load_memory_string(filename: str) -> str:
    input_path = pathlib.Path("data") / filename
    with open(input_path) as f_input:
        data = f_input.read().replace("\n", "")
    return data


def load_wordsearch_simple(filename: str) -> WordSearchSimple:
    input_path = pathlib.Path("data") / filename
    with open(input_path) as f_input:
        data = WordSearchSimple(f_input.readlines())
    return data


def load_wordsearch_array(filename: str) -> WordSearch:
    input_path = pathlib.Path("data") / filename
    with open(input_path) as f_input:
        lines = f_input.readlines()
    return WordSearch(lines)
