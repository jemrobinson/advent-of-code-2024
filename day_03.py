import logging
import time

from advent_of_code_2024.data_loaders import load_file_as_string
from advent_of_code_2024.parser import MemoryParser, parse_memory_string

def part_one():
    start = time.monotonic()
    memory = load_file_as_string("day-3.txt")
    instructions = parse_memory_string(memory)
    print("Day 3 part 1:", sum([x * y for x, y in instructions]), f"in {time.monotonic() - start:.3f} seconds")

def part_two():
    start = time.monotonic()
    memory = load_file_as_string("day-3.txt")
    parser = MemoryParser()
    print("Day 3 part 2:", parser.parse(memory), f"in {time.monotonic() - start:.3f} seconds")



if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR, format=r"[%(levelname)8s] %(message)s")
    part_one()
    part_two()