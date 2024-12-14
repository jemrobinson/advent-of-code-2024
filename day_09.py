from advent_of_code_2024.file_system import FileSystem

def part_one():
    file_system = FileSystem("day-9.txt")
    print("Day 9 part 1:", file_system.checksum())

def part_two():
    file_system = FileSystem("day-9.txt")
    print("Day 9 part 2:", file_system.checksum(strategy="conservative"))


if __name__ == "__main__":
    part_one()
    part_two()
