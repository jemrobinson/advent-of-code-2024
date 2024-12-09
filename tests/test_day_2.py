from advent_of_code_2024 import load_reports


def test_part_one():
    reports = load_reports("day-2.test.csv")
    assert sum([report.is_safe() for report in reports]) == 2
