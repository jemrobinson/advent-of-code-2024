import time

from advent_of_code_2024.lan_party import LanParty
from advent_of_code_2024.logic_gates import Computer


def part_one():
    start = time.monotonic()
    computer = Computer("day-24.txt")
    print("Day 24 part 1:", computer.run(), f"in {time.monotonic() - start:.3f} seconds")


def part_two():
    pass

if __name__ == "__main__":
    part_one()
    part_two()
