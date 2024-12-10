from collections.abc import Sequence
from typing import Any

import pandas as pd

from .utility import count


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


class WordSearch:
    def __init__(self, rows: Sequence[str]):
        size = len(rows)
        self.rows = [row.strip() for row in rows]
        self.columns = ["".join([row[idx] for row in rows]) for idx in range(len(rows))]
        self.diags_nwse = []
        self.diags_swne = []
        for idx_col in range(size):
            idx_row = 0
            chars_nwse = chars_swne = ""
            while idx_row + idx_col < size:
                chars_nwse += self.rows[idx_row][idx_row + idx_col]
                chars_swne += self.rows[size - idx_row - 1][idx_row + idx_col]
                idx_row += 1
            self.diags_nwse.append(chars_nwse)
            self.diags_swne.append(chars_swne)
        for idx_row in range(1, size):
            idx_col = 0
            chars_nwse = chars_swne = ""
            while idx_row + idx_col < size:
                chars_nwse += self.columns[idx_col][idx_row + idx_col]
                chars_swne += self.columns[idx_col][size - idx_row - idx_col - 1]
                idx_col += 1
            self.diags_nwse.append(chars_nwse)
            self.diags_swne.append(chars_swne)

    def search(self, pattern: str) -> int:
        pattern_r = pattern[::-1]
        rows = sum(count(pattern, row) for row in self.rows)
        rows_r = sum(count(pattern_r, row) for row in self.rows)
        columns = sum(count(pattern, column) for column in self.columns)
        columns_r = sum(count(pattern_r, column) for column in self.columns)
        diags_nwse = sum(count(pattern, diag_nwse) for diag_nwse in self.diags_nwse)
        diags_nwse_r = sum(count(pattern_r, diag_nwse) for diag_nwse in self.diags_nwse)
        diags_swne = sum(count(pattern, diag_swne) for diag_swne in self.diags_swne)
        diags_swne_r = sum(count(pattern_r, diag_swne) for diag_swne in self.diags_swne)
        return (
            rows
            + rows_r
            + columns
            + columns_r
            + diags_nwse
            + diags_nwse_r
            + diags_swne
            + diags_swne_r
        )
