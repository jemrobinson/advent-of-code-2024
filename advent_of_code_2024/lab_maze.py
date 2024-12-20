import copy

import numpy as np

from advent_of_code_2024.data_loaders import load_file_as_array
from advent_of_code_2024.grid_location import GridLocation, GridVector, grid_vectors
from advent_of_code_2024.matrix import StrMatrix


class Guard:
    def __init__(self, position: GridLocation, direction: GridVector) -> None:
        self.position = position
        self.direction = direction

    def next_position(self) -> GridLocation:
        return self.position + self.direction

    @property
    def state(self) -> tuple[GridLocation, GridVector]:
        return (self.position, self.direction)

    def turn(self) -> None:
        self.direction = self.direction.clockwise_90()


class LabMaze:
    def __init__(self, filename: str) -> None:
        self.matrix = StrMatrix(load_file_as_array(filename))
        self.guard = Guard(self.matrix.find("^")[0], grid_vectors["north"])
        self.visited: set[tuple[GridLocation, GridVector]] = set()

    def step(self) -> bool:
        """Take a step and return whether the guard has left the map."""
        # Raise an exception if we visit a previous state as this indicates a loop
        if self.guard.state in self.visited:
            msg = f"Found a loop at {self.guard.state}"
            raise StopIteration(msg)
        self.visited.add(self.guard.state)
        # If the next position is invalid we are leaving the map
        next_position = self.guard.next_position()
        if not next_position.in_bounds(*self.matrix.bounds()):
            return True
        # Otherwise update the map
        match self.matrix.get(next_position):
            case "." | "x":
                self.matrix.set(self.guard.position, "x")
                self.matrix.set(next_position, "@")
                self.guard.position = next_position
            case "#":
                self.guard.turn()
        return False

    def walk(self) -> int:
        while not self.step():
            pass
        counts: dict[str, int] = dict(
            zip(*np.unique(self.matrix.array, return_counts=True), strict=False)
        )
        return counts["x"] + counts["@"]

    def count_loops(self) -> int:
        n_loops = 0
        for location in self.matrix.locations():
            if self.matrix.get(location) == ".":
                maze = copy.deepcopy(self)
                maze.matrix.set(location, "#")
                try:
                    maze.walk()
                except StopIteration:
                    n_loops += 1
        return n_loops
