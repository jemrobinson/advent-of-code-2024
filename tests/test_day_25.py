from advent_of_code_2024.locks import LockKeyMatcher


def test_part_one():
    matcher = LockKeyMatcher("day-25.test.txt")
    assert matcher.unique_pairs() == 3
