from advent_of_code_2024.data_loaders import load_csv_as_df
from advent_of_code_2024.location_lists import distance_df, similarity_df


def test_part_one():
    df = load_csv_as_df("day-1.test.csv")
    assert distance_df(df) == 11


def test_part_two():
    df = load_csv_as_df("day-1.test.csv")
    assert similarity_df(df) == 31
