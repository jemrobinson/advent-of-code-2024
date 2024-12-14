import re
from functools import reduce
from operator import mul

from advent_of_code_2024.data_loaders import load_file_as_lines
from advent_of_code_2024.grid_location import GridLocation


class Robot:
    def __init__(self, state: str, width: int, height: int) -> None:
        result = re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", state)
        if not result:
            msg = f"Could not interpret {state}"
            raise ValueError(msg)
        self.position = GridLocation((int(result.group(1)), int(result.group(2))))
        self.velocity = GridLocation((int(result.group(3)), int(result.group(4))))
        self.width = width
        self.height = height
        self.total_steps = 0

    def move(self, n_steps: int) -> None:
        self.position = self.position + n_steps * self.velocity
        self.position.pos_0 = self.position.pos_0 % self.width
        self.position.pos_1 = self.position.pos_1 % self.height
        self.total_steps += n_steps


class RobotGrid:
    def __init__(self, filename: str, width: int, height: int) -> None:
        self.robots = [
            Robot(line, width, height) for line in load_file_as_lines(filename)
        ]
        centre_x, centre_y = (width - 1) // 2, (height - 1) // 2
        self.quadrants = [
            ((0, 0), (centre_x - 1, centre_y - 1)),
            ((centre_x + 1, 0), (width - 1, centre_y - 1)),
            ((0, centre_y + 1), (centre_x - 1, height - 1)),
            ((centre_x + 1, centre_y + 1), (width - 1, height - 1)),
        ]

    def count_robots(self, idx_quadrant: int) -> int:
        quadrant = self.quadrants[idx_quadrant]
        return sum(
            [
                (quadrant[0][0] <= robot.position.pos_0 <= quadrant[1][0])
                and (quadrant[0][1] <= robot.position.pos_1 <= quadrant[1][1])
                for robot in self.robots
            ]
        )

    def wait(self, n_steps: int) -> None:
        for robot in self.robots:
            robot.move(n_steps)

    def safety_factor(self, n_steps: int) -> int:
        self.wait(n_steps)
        return reduce(mul, [self.count_robots(idx) for idx in range(4)])
