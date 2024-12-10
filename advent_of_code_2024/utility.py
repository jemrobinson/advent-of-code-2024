import re
from collections.abc import Sequence


def as_int(input_string: str) -> int:
    return int("".join([char for char in input_string if char.isdigit()]))


def count(substring: str, string: str) -> int:
    return sum(
        [
            1 if string[idx:].startswith(substring) else 0
            for idx in range(len(string) - len(substring) + 1)
        ]
    )


def parse_memory_string(data: str) -> Sequence[tuple[int, int]]:
    matches: list[str] = re.findall(r"mul\(\d+,\d+\)", data)
    values = [[as_int(num) for num in match.split(",")] for match in matches]
    return [(value[0], value[1]) for value in values]
