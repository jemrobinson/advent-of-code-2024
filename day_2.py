#! /usr/bin/env python
from advent_of_code_2024 import load_reports

def part_one():
    reports = load_reports("day-2.csv")
    print(sum([report.is_safe() for report in reports]))

if __name__ == "__main__":
    part_one()
