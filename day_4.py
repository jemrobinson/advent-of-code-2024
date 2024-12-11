#! /usr/bin/env python
from advent_of_code_2024.wordsearch import WordSearch, WordSearchSimple


def part_one():
    wordsearch = WordSearchSimple("day-4.txt")
    print("Day 4 part 1:", wordsearch.search("XMAS"))

def part_two():
    wordsearch = WordSearch("day-4.txt")
    print("Day 4 part 2:", wordsearch.search_xmas())


if __name__ == "__main__":
    part_one()
    part_two()
