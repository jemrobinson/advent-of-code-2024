from collections.abc import Sequence
from typing import Any

import pandas as pd

from advent_of_code_2024.data_loaders import load_file_as_lines


class Report(pd.Series):  # type: ignore[type-arg]
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.threshold: int = 3

    def is_safe(self) -> bool:
        diffs: pd.Series[int] = self.diff()[1:]  # type: ignore[assignment]
        all_inc = diffs[diffs > 0].shape == diffs.shape
        all_dec = diffs[diffs < 0].shape == diffs.shape
        if not (all_inc or all_dec):
            return False
        if any(diffs.abs() > self.threshold):
            return False
        return True


class ReportWithDampener(pd.Series):  # type: ignore[type-arg]
    def is_safe(self) -> bool:
        for idx in range(self.size):
            subseries = self.drop(idx)
            if Report(subseries).is_safe():
                return True
        return False


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
