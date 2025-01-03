import time

from advent_of_code_2024.lab_maze import LabMaze


def part_one():
    start = time.monotonic()
    maze = LabMaze("day-6.txt")
    print("Day 6 part 1:", maze.walk(), f"in {time.monotonic() - start:.3f} seconds")


def part_two():
    start = time.monotonic()
    maze = LabMaze("day-6.txt")
    print("Day 6 part 2:",  maze.count_loops(), f"in {time.monotonic() - start:.3f} seconds")


if __name__ == "__main__":
    part_one()
    part_two()
