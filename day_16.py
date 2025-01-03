import time

from advent_of_code_2024.reindeer_maze import ReindeerMaze


def part_one():
    start = time.monotonic()
    maze = ReindeerMaze("day-16.txt")
    print("Day 16 part 1:", maze.shortest_path(), f"in {time.monotonic() - start:.3f} seconds")

def part_two():
    start = time.monotonic()
    maze = ReindeerMaze("day-16.txt")
    print("Day 16 part 2:", maze.best_seats(), f"in {time.monotonic() - start:.3f} seconds")

if __name__ == "__main__":
    part_one()
    part_two()
