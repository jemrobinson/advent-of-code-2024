import time

from advent_of_code_2024.three_bit_computer import ThreeBitComputer

def part_one():
    start = time.monotonic()
    computer = ThreeBitComputer("day-17.txt")
    print("Day 17 part 1:", computer.run(), f"in {time.monotonic() - start:.3f} seconds")

def part_two():
    start = time.monotonic()
    computer = ThreeBitComputer("day-17.txt")
    print("Day 17 part 1:", computer.find_register_a(), f"in {time.monotonic() - start:.3f} seconds")

if __name__ == "__main__":
    part_one()
    part_two()
