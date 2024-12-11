from advent_of_code_2024.data_loaders import read_csv
from advent_of_code_2024.metrics import distance_df, similarity_df


def test_part_one():
    df = read_csv("day-1.test.csv")
    assert distance_df(df) == 11


def test_part_two():
    df = read_csv("day-1.test.csv")
    assert similarity_df(df) == 31
