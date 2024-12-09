from typing import Any

import pandas as pd


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
