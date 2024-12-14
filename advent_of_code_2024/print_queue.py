from collections.abc import Sequence
from contextlib import suppress
from functools import cmp_to_key

from advent_of_code_2024.data_loaders import load_csv_as_df, load_file_as_lines


def evaluate_update(update: Sequence[int], rules: Sequence[tuple[int, int]]) -> bool:
    return all(evaluate_rule(update, rule) for rule in rules)


def evaluate_rule(update: Sequence[int], rule: tuple[int, int]) -> bool:
    with suppress(ValueError):
        idx_first = update.index(rule[0])
        idx_second = update.index(rule[1])
        if idx_second < idx_first:
            return False
    return True


def middle_page(update: Sequence[int]) -> int:
    if len(update) % 2 == 0:
        msg = f"No middle page for update of length {len(update)}"
        raise ValueError(msg)
    return update[len(update) // 2]


def sort_update(update: Sequence[int], rules: Sequence[tuple[int, int]]) -> list[int]:
    def comparator(x: int, y: int) -> int:
        for rule in rules:
            if rule[0] == x and rule[1] == y:
                return -1
            if rule[0] == y and rule[1] == x:
                return 1
        return 0

    return sorted(update, key=cmp_to_key(comparator))


def load_print_queue_rules(filename: str) -> Sequence[tuple[int, int]]:
    return [
        (int(row[0]), int(row[1]))
        for _, row in load_csv_as_df(filename, delimiter="|").iterrows()
    ]


def load_print_queue_updates(filename: str) -> Sequence[Sequence[int]]:
    return [list(map(int, line.split(","))) for line in load_file_as_lines(filename)]
