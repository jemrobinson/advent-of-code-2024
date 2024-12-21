import time

from advent_of_code_2024.keypad import KeypadSolver


def part_one():
    start = time.monotonic()
    solver = KeypadSolver("day-21.txt")
    print("Day 21 part 1:", solver.total_complexity(), f"in {time.monotonic() - start:.3f} seconds")


def part_two():
    pass

if __name__ == "__main__":
    part_one()
    part_two()
