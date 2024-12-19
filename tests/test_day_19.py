from advent_of_code_2024.towels import Towels


def test_part_one():
    towels = Towels("day-19-patterns.test.txt", "day-19-designs.test.txt")
    assert towels.count_possible() == 6


def test_part_two():
    towels = Towels("day-19-patterns.test.txt", "day-19-designs.test.txt")
    assert towels.count_combinations() == 16
