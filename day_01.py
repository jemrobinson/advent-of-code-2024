#! /usr/bin/env python
from advent_of_code_2024.data_loaders import load_csv_as_df
from advent_of_code_2024.location_lists import distance_df, similarity_df

def part_one():
    df = load_csv_as_df("day-1.csv")
    print("Day 1 part 1:", distance_df(df))

def part_two():
    df = load_csv_as_df("day-1.csv")
    print("Day 1 part 2:", similarity_df(df))

if __name__ == "__main__":
    part_one()
    part_two()
