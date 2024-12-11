#! /usr/bin/env python
from advent_of_code_2024.data_loaders import load_reports, load_reports_with_dampener

def part_one():
    reports = load_reports("day-2.csv")
    print(sum([report.is_safe() for report in reports]))

def part_two():
    reports = load_reports_with_dampener("day-2.csv")
    print(sum([report.is_safe() for report in reports]))


if __name__ == "__main__":
    part_one()
    part_two()