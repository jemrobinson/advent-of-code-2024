import time

from advent_of_code_2024.data_loaders import load_csv_as_df
from advent_of_code_2024.location_lists import distance_df, similarity_df

def part_one():
    start = time.monotonic()
    df = load_csv_as_df("day-1.csv")
    print("Day 1 part 1:", distance_df(df), f"in {time.monotonic() - start:.3f} seconds")

def part_two():
    start = time.monotonic()
    df = load_csv_as_df("day-1.csv")
    print("Day 1 part 2:", similarity_df(df), f"in {time.monotonic() - start:.3f} seconds")

if __name__ == "__main__":
    part_one()
    part_two()
