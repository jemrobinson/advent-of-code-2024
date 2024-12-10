#! /usr/bin/env python
from advent_of_code_2024 import load_memory_string

def part_one():
    instructions = load_memory_string("day-3.txt")
    print(sum([x * y for x, y in instructions]))

def part_two():
    pass


if __name__ == "__main__":
    part_one()
    part_two()