from advent_of_code_2024 import load_wordsearch


def test_part_one():
    data = load_wordsearch("day-4.test.txt")
    assert data.search("XMAS") == 18
