def as_int(input_string: str) -> int:
    return int("".join([char for char in input_string if char.isdigit()]))


def count(substring: str, string: str) -> int:
    return sum(
        [
            1 if string[idx:].startswith(substring) else 0
            for idx in range(len(string) - len(substring) + 1)
        ]
    )
