from advent_of_code_2024.robots import RobotGrid


def test_part_one():
    assert grid.safety_factor(100) == 12

def part_one():
    grid = RobotGrid("day-14.txt", width=101, height=103)
    print("Day 14 part 1:", grid.safety_factor(100))

def part_two():
    pass

if __name__ == "__main__":
    part_one()
    part_two()
