from advent_of_code_2024.reindeer_maze import ReindeerMaze


def test_part_one():
    maze_0 = ReindeerMaze("day-16.test-0.txt")
    assert maze_0.shortest_path() == 7036
    maze_1 = ReindeerMaze("day-16.test-1.txt")
    assert maze_1.shortest_path() == 11048


def test_part_two():
    pass
