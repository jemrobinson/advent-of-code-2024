import copy
import enum

import numpy as np

from advent_of_code_2024.array import StrArray2D
from advent_of_code_2024.data_loaders import load_file_as_array
from advent_of_code_2024.grid_location import GridLocation


class Direction(enum.IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Guard:
    def __init__(self, position: GridLocation, direction: Direction) -> None:
        self.position = position
        self.direction = direction

    def next_position(self) -> GridLocation:
        pos_0, pos_1 = self.position.as_tuple()
        if self.direction == Direction.NORTH:
            return GridLocation((pos_0 - 1, pos_1))
        if self.direction == Direction.EAST:
            return GridLocation((pos_0, pos_1 + 1))
        if self.direction == Direction.SOUTH:
            return GridLocation((pos_0 + 1, pos_1))
        if self.direction == Direction.WEST:
            return GridLocation((pos_0, pos_1 - 1))

    @property
    def state(self) -> tuple[GridLocation, Direction]:
        return (self.position, self.direction)

    def turn(self) -> None:
        self.direction = Direction((self.direction + 1) % len(Direction))


class LabMaze:
    def __init__(self, filename: str) -> None:
        self.array = StrArray2D(load_file_as_array(filename))
        self.bounds = (
            int(self.array.array.shape[0] - 1),
            int(self.array.array.shape[1] - 1),
        )
        self.guard = Guard(self.array.find("^")[0], Direction.NORTH)
        self.visited: set[tuple[GridLocation, Direction]] = set()

    def step(self) -> bool:
        """Take a step and return whether the guard has left the map."""
        # Raise an exception if we visit a previous state as this indicates a loop
        if self.guard.state in self.visited:
            msg = f"Found a loop at {self.guard.state}"
            raise StopIteration(msg)
        self.visited.add(self.guard.state)
        # If the next position is invalid we are leaving the map
        next_position = self.guard.next_position()
        if not next_position.in_bounds(*self.bounds):
            return True
        # Otherwise update the map
        match self.array.get(next_position):
            case "." | "x":
                self.array.set(self.guard.position, "x")
                self.array.set(next_position, "@")
                self.guard.position = next_position
            case "#":
                self.guard.turn()
        return False

    def walk(self) -> int:
        while not self.step():
            pass
        counts: dict[str, int] = dict(
            zip(*np.unique(self.array.array, return_counts=True), strict=False)
        )
        return counts["x"] + counts["@"]

    def count_loops(self) -> int:
        n_loops = 0
        for location in self.array.locations():
            if self.array.get(location) == ".":
                maze = copy.deepcopy(self)
                maze.array.set(location, "#")
                try:
                    maze.walk()
                except StopIteration:
                    n_loops += 1
        return n_loops
