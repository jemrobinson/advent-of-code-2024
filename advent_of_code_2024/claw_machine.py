from collections.abc import Sequence
from itertools import batched

import numpy as np

from advent_of_code_2024.data_loaders import load_file_as_lines
from advent_of_code_2024.grid_location import GridLocation


class ClawMachine:
    def __init__(
        self, lines: Sequence[str], offset: int, *, cost_a: int = 3, cost_b: int = 1
    ) -> None:
        self.button_a = GridLocation(
            [int(cmd.split("+")[1]) for cmd in (lines[0].split(":")[1].split(","))]
        )
        self.button_b = GridLocation(
            [int(cmd.split("+")[1]) for cmd in (lines[1].split(":")[1].split(","))]
        )
        self.cost_a = cost_a
        self.cost_b = cost_b
        self.prize = GridLocation(
            [
                int(cmd.split("=")[1]) + offset
                for cmd in (lines[2].split(":")[1].split(","))
            ]
        )

    def solve(self, *, use_brute_force: bool = False) -> tuple[int, int, int] | None:
        if use_brute_force:
            return self.brute_force()
        return self.algebra()

    def algebra(self) -> tuple[int, int, int] | None:
        a_x, a_y = self.button_a.as_tuple()
        b_x, b_y = self.button_b.as_tuple()
        p_x, p_y = self.prize.as_tuple()
        # Solve for (n_presses_a, n_presses_b):
        #   n_presses_a * a_x + n_presses_b * b_x = p_x
        #   n_presses_a * a_y + n_presses_b * b_y = p_y
        lhs = np.array([[a_x, b_x], [a_y, b_y]])
        rhs = np.array([p_x, p_y])
        # Result might have non-integer solutions
        result = np.linalg.solve(lhs, rhs)
        n_presses_a, n_presses_b = int(round(result[0])), int(round(result[1]))
        # Check whether the rounded result is valid
        if self.is_valid(n_presses_a, n_presses_b):
            return (n_presses_a, n_presses_b, self.cost(n_presses_a, n_presses_b))
        return None

    def brute_force(self) -> tuple[int, int, int] | None:
        solutions = []
        for n_presses_a in range(101):
            for n_presses_b in range(101):
                if self.is_valid(n_presses_a, n_presses_b):
                    solutions.append(
                        (n_presses_a, n_presses_b, self.cost(n_presses_a, n_presses_b))
                    )
        if not solutions:
            return None
        return sorted(solutions, key=lambda t: t[2])[0]

    def cost(self, n_presses_a: int, n_presses_b: int) -> int:
        return n_presses_a * self.cost_a + n_presses_b * self.cost_b

    def is_valid(self, n_presses_a: int, n_presses_b: int) -> bool:
        return n_presses_a * self.button_a + n_presses_b * self.button_b == self.prize


def get_claw_machines(filename: str, offset: int = 0) -> list[ClawMachine]:
    lines = load_file_as_lines(filename)
    return [ClawMachine(instructions, offset) for instructions in batched(lines, 4)]
