from advent_of_code_2024.data_loaders import load_memory_string
from advent_of_code_2024.parser import MemoryParser, parse_memory_string


def test_part_one():
    memory = load_memory_string("day-3.test-1.txt")
    instructions = parse_memory_string(memory)
    assert (sum([x * y for x, y in instructions])) == 161


def test_part_two():
    memory = load_memory_string("day-3.test-2.txt")
    parser = MemoryParser()
    assert parser.parse(memory) == 48
