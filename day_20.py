import time

from advent_of_code_2024.race_condition_maze import RaceConditionMaze


def part_one():
    start = time.monotonic()
    maze = RaceConditionMaze("day-20.txt")
    print("Day 20 part 1:", maze.n_cheats(n_picoseconds_disabled=2, minimum_time_saved=100), f"in {time.monotonic() - start:.3f} seconds")


def part_two():
    start = time.monotonic()
    maze = RaceConditionMaze("day-20.txt")
    print("Day 20 part 2:", maze.n_cheats(n_picoseconds_disabled=20, minimum_time_saved=100), f"in {time.monotonic() - start:.3f} seconds")

if __name__ == "__main__":
    part_one()
    part_two()
