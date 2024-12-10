from advent_of_code_2024 import load_memory_string


def test_part_one():
    instructions = load_memory_string("day-3.test.txt")
    assert (sum([x * y for x, y in instructions])) == 161
