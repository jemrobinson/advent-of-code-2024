import time

from advent_of_code_2024.towels import Towels


def part_one():
    start = time.monotonic()
    towels = Towels("day-19-patterns.txt", "day-19-designs.txt")
    print("Day 19 part 1:", towels.count_possible(), f"in {time.monotonic() - start:.3f} seconds")


def part_two():
    pass

if __name__ == "__main__":
    part_one()
    part_two()
