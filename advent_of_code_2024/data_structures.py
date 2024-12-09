import pandas as pd


class Report(pd.Series[int]):
    def is_safe(self, threshold: int = 3) -> bool:
        diffs = self.diff()[1:]
        all_inc = diffs[diffs > 0].shape == diffs.shape
        all_dec = diffs[diffs < 0].shape == diffs.shape
        if not (all_inc or all_dec):
            return False
        if any(diffs.abs() > threshold):
            return False
        return True
