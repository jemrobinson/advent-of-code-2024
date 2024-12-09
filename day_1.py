#! /usr/bin/env python
from advent_of_code_2024 import read_csv, df_distance

def part_one():
    df = read_csv("day-1.csv")
    print(df_distance(df))

if __name__ == "__main__":
    part_one()
