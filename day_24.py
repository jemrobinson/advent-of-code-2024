import time

from advent_of_code_2024.logic_gates import Computer


def part_one():
    start = time.monotonic()
    computer = Computer("day-24.txt")
    print("Day 24 part 1:", computer.output(), f"in {time.monotonic() - start:.3f} seconds")


def part_two():
    start = time.monotonic()
    computer = Computer("day-24.txt")
    print("Day 24 part 2:", computer.calculate_swaps(), f"in {time.monotonic() - start:.3f} seconds")

if __name__ == "__main__":
    part_one()
    part_two()
