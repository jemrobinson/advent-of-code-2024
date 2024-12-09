from advent_of_code_2024 import distance_df, read_csv, similarity_df


def test_part_one():
    df = read_csv("day-1.test.csv")
    assert distance_df(df) == 11


def test_part_two():
    df = read_csv("day-1.test.csv")
    assert similarity_df(df) == 31
