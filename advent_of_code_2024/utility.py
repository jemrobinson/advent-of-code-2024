def as_int(input_string: str) -> int:
    return int("".join([char for char in input_string if char.isdigit()]))
