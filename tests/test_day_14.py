from advent_of_code_2024.robots import RobotGrid


def test_part_one():
    grid = RobotGrid("day-14.test.txt", width=11, height=7)
    assert grid.safety_factor(100) == 12
