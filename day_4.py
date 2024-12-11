#! /usr/bin/env python
from advent_of_code_2024.data_loaders import load_wordsearch_array, load_wordsearch_simple


def part_one():
    data = load_wordsearch_simple("day-4.txt")
    print(data.search("XMAS"))

def part_two():
    data = load_wordsearch_array("day-4.txt")
    print(data.search_xmas())


if __name__ == "__main__":
    part_one()
    part_two()