from collections.abc import Sequence
from itertools import batched

from .data_loaders import load_file_as_lines
from .grid_location import GridLocation


class ClawMachine:
    def __init__(self, lines: Sequence[str], cost_a: int = 3, cost_b: int = 1) -> None:
        self.button_a = GridLocation(
            [int(cmd.split("+")[1]) for cmd in (lines[0].split(":")[1].split(","))]
        )
        self.button_b = GridLocation(
            [int(cmd.split("+")[1]) for cmd in (lines[1].split(":")[1].split(","))]
        )
        self.cost_a = cost_a
        self.cost_b = cost_b
        self.prize = GridLocation(
            [int(cmd.split("=")[1]) for cmd in (lines[2].split(":")[1].split(","))]
        )

    def solve(self) -> tuple[int, int, int] | None:
        solutions = []
        for n_presses_a in range(101):
            for n_presses_b in range(101):
                if (
                    n_presses_a * self.button_a + n_presses_b * self.button_b
                    == self.prize
                ):
                    solutions.append(
                        (n_presses_a, n_presses_b, self.cost(n_presses_a, n_presses_b))
                    )
        if not solutions:
            return None
        return sorted(solutions, key=lambda t: t[2])[0]

    def cost(self, n_presses_a: int, n_presses_b: int) -> int:
        return n_presses_a * self.cost_a + n_presses_b * self.cost_b


def get_claw_machines(filename: str) -> list[ClawMachine]:
    lines = load_file_as_lines(filename)
    return [ClawMachine(instructions) for instructions in batched(lines, 4)]
