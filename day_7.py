#! /usr/bin/env python
from advent_of_code_2024.calibration import Calibration
from advent_of_code_2024.data_loaders import load_file_as_lines


def part_one():
    calibrations = [Calibration(line) for line in load_file_as_lines("day-7.txt")]
    total = sum([calibration.output for calibration in calibrations if calibration.is_valid()])
    print("Day 7 part 1:", total)

def part_two():
    pass


if __name__ == "__main__":
    part_one()
    part_two()
