from advent_of_code_2024.calibration import Calibration
from advent_of_code_2024.data_loaders import load_file_as_lines


def test_part_one():
    calibrations = [Calibration(line) for line in load_file_as_lines("day-7.test.txt")]
    assert (
        sum(
            [
                calibration.output
                for calibration in calibrations
                if calibration.is_valid()
            ]
        )
        == 3749
    )


def test_part_two():
    pass
