import time
from advent_of_code_2024.robots import RobotGrid

def part_one():
    start = time.monotonic()
    grid = RobotGrid("day-14.txt", width=101, height=103)
    print("Day 14 part 1:", grid.safety_factor(100), f"in {time.monotonic() - start:.3f} seconds")

def part_two():
    start = time.monotonic()
    grid = RobotGrid("day-14.txt", width=101, height=103)
    print("Day 14 part 2:", grid.christmas_tree(), f"in {time.monotonic() - start:.3f} seconds")
    start = time.monotonic()
    grid = RobotGrid("day-14.txt", width=101, height=103)
    print("Day 14 part 2:", grid.christmas_tree_adjacency(500), f"in {time.monotonic() - start:.3f} seconds")
    start = time.monotonic()
    grid = RobotGrid("day-14.txt", width=101, height=103)
    print("Day 14 part 2:", grid.christmas_tree_non_adjacency(1000), f"in {time.monotonic() - start:.3f} seconds")

if __name__ == "__main__":
    part_one()
    part_two()
