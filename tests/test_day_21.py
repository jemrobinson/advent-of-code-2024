from advent_of_code_2024.keypad import KeypadSolver


def test_part_one():
    solver = KeypadSolver("day-21.test.txt")
    assert solver.complexity(solver.codes[0]) == 68 * 29
    assert solver.complexity(solver.codes[1]) == 60 * 980
    assert solver.complexity(solver.codes[2]) == 68 * 179
    assert solver.complexity(solver.codes[3]) == 64 * 456
    assert solver.complexity(solver.codes[4]) == 64 * 379
    assert solver.total_complexity() == 126384


def test_part_two():
    pass
