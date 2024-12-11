#! /usr/bin/env python
from advent_of_code_2024.data_loaders import read_csv
from advent_of_code_2024.metrics import distance_df, similarity_df

def part_one():
    df = read_csv("day-1.csv")
    print(distance_df(df))

def part_two():
    df = read_csv("day-1.csv")
    print(similarity_df(df))

if __name__ == "__main__":
    part_one()
    part_two()
