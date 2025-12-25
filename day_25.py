import time

from advent_of_code_2024.locks import LockKeyMatcher


def part_one():
    start = time.monotonic()
    matcher = LockKeyMatcher("day-25.txt")
    print("Day 25 part 1:", matcher.unique_pairs(), f"in {time.monotonic() - start:.3f} seconds")


if __name__ == "__main__":
    part_one()
