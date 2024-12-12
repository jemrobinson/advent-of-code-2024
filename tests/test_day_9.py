from advent_of_code_2024.file_system import FileSystem


def test_part_one():
    file_system = FileSystem("day-9.test.txt")
    assert file_system.checksum() == 1928


def test_part_two():
    pass
