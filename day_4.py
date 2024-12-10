#! /usr/bin/env python
from advent_of_code_2024 import load_wordsearch


def part_one():
    data = load_wordsearch("day-4.txt")
    print(data.search("XMAS"))

def part_two():
    pass


if __name__ == "__main__":
    part_one()
    part_two()