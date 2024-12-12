from advent_of_code_2024.data_loaders import load_reports, load_reports_with_dampener


def test_part_one():
    reports = load_reports("day-2.test.csv")
    assert sum([report.is_safe() for report in reports]) == 2


def test_part_two():
    reports = load_reports_with_dampener("day-2.test.csv")
    assert sum([report.is_safe() for report in reports]) == 4
