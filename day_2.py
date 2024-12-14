#! /usr/bin/env python
from advent_of_code_2024.report import load_reports, load_reports_with_dampener

def part_one():
    reports = load_reports("day-2.csv")
    print("Day 2 part 1:", sum([report.is_safe() for report in reports]))

def part_two():
    reports = load_reports_with_dampener("day-2.csv")
    print("Day 2 part 2:", sum([report.is_safe() for report in reports]))


if __name__ == "__main__":
    part_one()
    part_two()