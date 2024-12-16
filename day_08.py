import time
from functools import reduce

from advent_of_code_2024.antennae import load_antenna_sets


def part_one():
    start = time.monotonic()
    antennae = load_antenna_sets("day-8.txt")
    antinodes = reduce(set.union, [a.antinodes() for a in antennae])
    print("Day 8 part 1:", len(antinodes), f"in {time.monotonic() - start:.3f} seconds")

def part_two():
    start = time.monotonic()
    antennae = load_antenna_sets("day-8.txt")
    antinodes = reduce(
        set.union, [a.antinodes(first_harmonic=0, last_harmonic=999) for a in antennae]
    )
    print("Day 8 part 2:", len(antinodes), f"in {time.monotonic() - start:.3f} seconds")


if __name__ == "__main__":
    part_one()
    part_two()
