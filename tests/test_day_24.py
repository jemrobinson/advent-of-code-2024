from advent_of_code_2024.logic_gates import Computer


def test_part_one():
    computer_0 = Computer("day-24.test-0.txt")
    assert computer_0.run() == 4
    computer_1 = Computer("day-24.test-1.txt")
    assert computer_1.run() == 2024


def test_part_two():
    pass
