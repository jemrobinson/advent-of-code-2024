from advent_of_code_2024.data_loaders import (
    load_wordsearch_array,
    load_wordsearch_simple,
)


def test_part_one():
    data = load_wordsearch_simple("day-4.test.txt")
    assert data.search("XMAS") == 18


def test_part_two():
    data = load_wordsearch_array("day-4.test.txt")
    assert data.search_xmas() == 9
