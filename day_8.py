#! /usr/bin/env python
from functools import reduce

from advent_of_code_2024.antennae import load_antenna_sets


def part_one():
    antennae = load_antenna_sets("day-8.txt")
    antinodes = reduce(set.union, [a.antinodes() for a in antennae])
    print("Day 8 part 1:", len(antinodes))

def part_two():
    print("Day 8 part 2:")


if __name__ == "__main__":
    part_one()
    part_two()
