from advent_of_code_2024.three_bit_computer import ThreeBitComputer


def test_part_one():
    computer = ThreeBitComputer("day-17.test.txt")
    assert computer.run() == [4, 6, 3, 5, 6, 3, 5, 2, 1, 0]


def test_part_two():
    pass
