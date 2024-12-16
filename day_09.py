import time
from advent_of_code_2024.file_system import FileSystem

def part_one():
    start = time.monotonic()
    file_system = FileSystem("day-9.txt")
    print("Day 9 part 1:", file_system.checksum(), f"in {time.monotonic() - start:.3f} seconds")

def part_two():
    start = time.monotonic()
    file_system = FileSystem("day-9.txt")
    print("Day 9 part 2:", file_system.checksum(strategy="conservative"), f"in {time.monotonic() - start:.3f} seconds")


if __name__ == "__main__":
    part_one()
    part_two()
