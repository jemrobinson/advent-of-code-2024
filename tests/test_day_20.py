from advent_of_code_2024.race_condition_maze import RaceConditionMaze


def test_part_one():
    maze = RaceConditionMaze("day-20.test.txt")
    assert maze.n_cheats(minimum_time_saved=2) == 44
    assert maze.n_cheats(minimum_time_saved=10) == 10
    assert maze.n_cheats(minimum_time_saved=20) == 5
    assert maze.n_cheats(minimum_time_saved=30) == 4
    assert maze.n_cheats(minimum_time_saved=40) == 2
    assert maze.n_cheats(minimum_time_saved=50) == 1


def test_part_two():
    pass
