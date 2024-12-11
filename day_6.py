#! /usr/bin/env python
from advent_of_code_2024.maze import Maze


def part_one():
    maze = Maze("day-6.txt")
    print("Day 6 part 1:", maze.walk())


def part_two():
    maze = Maze("day-6.txt")
    print("Day 6 part 2:",  maze.count_loops())


if __name__ == "__main__":
    part_one()
    part_two()
