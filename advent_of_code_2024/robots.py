import re
from functools import reduce
from operator import mul

from advent_of_code_2024.data_loaders import load_file_as_lines
from advent_of_code_2024.grid_location import GridLocation


class Robot:
    def __init__(self, state: str) -> None:
        result = re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", state)
        if not result:
            msg = f"Could not interpret {state}"
            raise ValueError(msg)
        self.position = GridLocation((int(result.group(1)), int(result.group(2))))
        self.velocity = GridLocation((int(result.group(3)), int(result.group(4))))

    def move(self, n_steps: int, max_width: int, max_height: int) -> None:
        self.position = self.position + n_steps * self.velocity
        self.position.pos_0 = self.position.pos_0 % max_width
        self.position.pos_1 = self.position.pos_1 % max_height


class RobotGrid:
    def __init__(self, filename: str, width: int, height: int) -> None:
        self.robots = [Robot(line) for line in load_file_as_lines(filename)]
        centre_x, centre_y = (width - 1) // 2, (height - 1) // 2
        self.quadrants = [
            ((0, 0), (centre_x - 1, centre_y - 1)),
            ((centre_x + 1, 0), (width - 1, centre_y - 1)),
            ((0, centre_y + 1), (centre_x - 1, height - 1)),
            ((centre_x + 1, centre_y + 1), (width - 1, height - 1)),
        ]
        self.width = width
        self.height = height

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
            robot.move(n_steps, max_width=self.width, max_height=self.height)

    def safety_factor(self, n_steps: int) -> int:
        self.wait(n_steps)
        return reduce(mul, [self.count_robots(idx) for idx in range(4)])

    def draw_positions(self) -> list[str]:
        lines = []
        robot_locations = {robot.position.as_tuple() for robot in self.robots}
        for iy in range(self.height):
            line = ""
            for ix in range(self.width):
                line += "X" if (ix, iy) in robot_locations else "."
            lines.append(line + "\n")
        return lines

    def christmas_tree(self) -> int:
        # Assume that a Christmas tree will have this shape somewhere in it
        pattern = (
            "...X...",
            "..XXX..",
            ".XXXXX.",
            "XXXXXXX",
        )
        idx_step = 0
        while True:
            # Find out where the robots are
            lines = self.draw_positions()

            # Check (loosely) for pattern existence
            draw = False
            for idx in range(len(lines) - len(pattern) + 1):
                if all(
                    pattern[idx_p] in lines[idx + idx_p]
                    for idx_p in range(len(pattern))
                ):
                    draw = True

            # Draw the positions if we got a match
            if draw:
                with open(f"trees/robots_{idx_step}.txt", "w") as f_out:
                    f_out.writelines(self.draw_positions())
                return idx_step

            # Take a step
            self.wait(1)
            idx_step += 1
