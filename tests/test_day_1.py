from advent_of_code_2024 import df_distance, read_csv


def test_part_one():
    df = read_csv("day-1.test.csv")
    assert df_distance(df) == 11
