#! /usr/bin/env python
import logging

from advent_of_code_2024.data_loaders import load_memory_string
from advent_of_code_2024.parser import MemoryParser, parse_memory_string

def part_one():
    memory = load_memory_string("day-3.txt")
    instructions = parse_memory_string(memory)
    print(sum([x * y for x, y in instructions]))

def part_two():
    memory = load_memory_string("day-3.txt")
    parser = MemoryParser()
    print(parser.parse(memory))



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format=r"[%(levelname)8s] %(message)s")
    part_one()
    part_two()