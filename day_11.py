import time
from advent_of_code_2024.stones import StoneLine

def part_one():
    start = time.monotonic()
    stone_line = StoneLine("day-11.txt")
    print("Day 11 part 1:", stone_line.score(25), f"in {time.monotonic() - start:.3f} seconds")

def part_two():
    start = time.monotonic()
    stone_line = StoneLine("day-11.txt")
    print("Day 11 part 2:", stone_line.score(75), f"in {time.monotonic() - start:.3f} seconds")


if __name__ == "__main__":
    part_one()
    part_two()
