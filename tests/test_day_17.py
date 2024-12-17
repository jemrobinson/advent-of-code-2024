from advent_of_code_2024.three_bit_computer import ThreeBitComputer


def test_part_one():
    computer = ThreeBitComputer("day-17.test-0.txt")
    assert computer.run() == [4, 6, 3, 5, 6, 3, 5, 2, 1, 0]


def test_part_two():
    computer = ThreeBitComputer("day-17.test-1.txt")
    assert computer.find_register_a() == 117440
