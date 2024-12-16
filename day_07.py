import time

from advent_of_code_2024.calibration import CalibrationFull, CalibrationSimple
from advent_of_code_2024.data_loaders import load_file_as_lines


def part_one():
    start = time.monotonic()
    calibrations = [CalibrationSimple(line) for line in load_file_as_lines("day-7.txt")]
    total = sum([calibration.output for calibration in calibrations if calibration.is_valid()])
    print("Day 7 part 1:", total, f"in {time.monotonic() - start:.3f} seconds")

def part_two():
    start = time.monotonic()
    calibrations = [CalibrationFull(line) for line in load_file_as_lines("day-7.txt")]
    total = sum([calibration.output for calibration in calibrations if calibration.is_valid()])
    print("Day 7 part 2:", total, f"in {time.monotonic() - start:.3f} seconds")


if __name__ == "__main__":
    part_one()
    part_two()
