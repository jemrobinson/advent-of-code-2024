from advent_of_code_2024.wordsearch import WordSearch, WordSearchSimple


def test_part_one():
    wordsearch = WordSearchSimple("day-4.test.txt")
    assert wordsearch.search("XMAS") == 18


def test_part_two():
    wordsearch = WordSearch("day-4.test.txt")
    assert wordsearch.search_xmas() == 9
