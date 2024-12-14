from collections import defaultdict
from functools import cache

from advent_of_code_2024.data_loaders import load_file_as_string


@cache
def blink(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    value_str = str(stone)
    if len(value_str) % 2 == 0:
        return [
            int(value_str[: len(value_str) // 2]),
            int(value_str[len(value_str) // 2 :]),
        ]
    return [stone * 2024]


class StoneLine:
    def __init__(self, filename: str) -> None:
        data = load_file_as_string(filename).split()
        self.stone_counts: dict[int, int] = defaultdict(int)
        for value in data:
            self.stone_counts[int(value)] += 1

    def score(self, n_blinks: int) -> int:
        for _ in range(n_blinks):
            new_counts: dict[int, int] = defaultdict(int)
            for value, count in self.stone_counts.items():
                for new_value in blink(value):
                    new_counts[new_value] += count
            self.stone_counts = new_counts
        return sum(self.stone_counts.values())
