from functools import reduce
from operator import iadd

from .data_loaders import load_file_as_string


class Stone:
    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"Stone({self.value})"

    def blink(self) -> list["Stone"]:
        if self.value == 0:
            return [Stone(1)]
        value_str = str(self.value)
        if len(value_str) % 2 == 0:
            return [
                Stone(int(value_str[: len(value_str) // 2])),
                Stone(int(value_str[len(value_str) // 2 :])),
            ]
        return [Stone(self.value * 2024)]


class StoneLine:
    def __init__(self, filename: str) -> None:
        data = load_file_as_string(filename).split()
        self.stones = [Stone(int(value)) for value in data]

    def blink(self) -> None:
        stones = [stone.blink() for stone in self.stones]
        self.stones = reduce(iadd, stones, [])

    def score(self, n_blinks: int) -> int:
        for _ in range(n_blinks):
            self.blink()
        return len(self.stones)
