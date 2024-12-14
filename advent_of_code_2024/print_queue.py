from collections.abc import Sequence
from contextlib import suppress
from functools import cmp_to_key

import pandas as pd

from advent_of_code_2024.data_loaders import load_csv_as_df, load_file_as_lines


class OrderingRule:
    def __init__(self, rule: pd.Series) -> None:  # type: ignore[type-arg]
        self.first = int(rule[0])
        self.second = int(rule[1])


class PageList:
    def __init__(self, line: str) -> None:
        self.page_list = list(map(int, line.split(",")))

    def apply(self, rules: Sequence[OrderingRule]) -> "PageList":
        def comparator(x: int, y: int) -> int:
            for rule in rules:
                if rule.first == x and rule.second == y:
                    return -1
                if rule.first == y and rule.second == x:
                    return 1
            return 0

        self.page_list.sort(key=cmp_to_key(comparator))
        return self

    def evaluate_rule(self, rule: OrderingRule) -> bool:
        with suppress(ValueError):
            idx_first = self.page_list.index(rule.first)
            idx_second = self.page_list.index(rule.second)
            if idx_second < idx_first:
                return False
        return True

    def is_ordered(self, rules: Sequence[OrderingRule]) -> bool:
        return all(self.evaluate_rule(rule) for rule in rules)

    def middle_page(self) -> int:
        if len(self.page_list) % 2 == 0:
            msg = f"No middle page for update of length {len(self.page_list)}"
            raise ValueError(msg)
        return self.page_list[len(self.page_list) // 2]


class PrintQueue:
    def __init__(self, rules_file: str, updates_file: str) -> None:
        self.rules = [
            OrderingRule(row)
            for _, row in load_csv_as_df(rules_file, delimiter="|").iterrows()
        ]
        self.updates = [PageList(line) for line in load_file_as_lines(updates_file)]

    def score_ordered_updates(self) -> int:
        return sum(
            [
                update.middle_page()
                for update in self.updates
                if update.is_ordered(self.rules)
            ]
        )

    def score_unordered_updates(self) -> int:
        return sum(
            update.apply(self.rules).middle_page()
            for update in self.updates
            if not update.is_ordered(self.rules)
        )
