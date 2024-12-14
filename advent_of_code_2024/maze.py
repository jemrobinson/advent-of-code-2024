import copy
import enum

import numpy as np

from advent_of_code_2024.data_loaders import load_file_as_array

Position = tuple[int, int]


class Direction(enum.IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Guard:
    def __init__(self, position: Position, direction: Direction) -> None:
        self.position = position
        self.direction = direction

    def next_position(self) -> Position:
        pos_0, pos_1 = self.position
        if self.direction == Direction.NORTH:
            return (pos_0 - 1, pos_1)
        if self.direction == Direction.EAST:
            return (pos_0, pos_1 + 1)
        if self.direction == Direction.SOUTH:
            return (pos_0 + 1, pos_1)
        if self.direction == Direction.WEST:
            return (pos_0, pos_1 - 1)

    @property
    def state(self) -> tuple[Position, Direction]:
        return (self.position, self.direction)

    def turn(self) -> None:
        self.direction = Direction((self.direction + 1) % len(Direction))


class Maze:
    def __init__(self, filename: str) -> None:
        self.array = load_file_as_array(filename)
        coords = [int(coord) for coord in np.where(self.array == "^")]
        self.guard = Guard((coords[0], coords[1]), Direction.NORTH)
        self.visited: set[tuple[Position, Direction]] = set()

    def mark(self, position: Position, value: str) -> None:
        self.array[position[0], position[1]] = value

    def value(self, position: Position) -> str:
        return str(self.array[position[0], position[1]])

    def step(self) -> bool:
        """Take a step and return whether the guard has left the map."""
        # Raise an exception if we visit a previous state as this indicates a loop
        if self.guard.state in self.visited:
            msg = f"Found a loop at {self.guard.state}"
            raise StopIteration(msg)
        self.visited.add(self.guard.state)
        # If the next position is invalid we are leaving the map
        next_position = self.guard.next_position()
        if not (
            (0 <= next_position[0] < self.array.shape[0])
            and (0 <= next_position[1] < self.array.shape[1])
        ):
            return True
        # Otherwise update the map
        match self.value(next_position):
            case "." | "x":
                self.mark(self.guard.position, "x")
                self.mark(next_position, "@")
                self.guard.position = next_position
            case "#":
                self.guard.turn()
        return False

    def walk(self) -> int:
        while not self.step():
            pass
        counts: dict[str, int] = dict(
            zip(*np.unique(self.array, return_counts=True), strict=False)
        )
        return counts["x"] + counts["@"]

    def count_loops(self) -> int:
        n_loops = 0
        for position in np.ndindex(self.array.shape):
            if self.value(position) == ".":  # type: ignore[arg-type]
                maze = copy.deepcopy(self)
                maze.mark(position, "#")  # type: ignore[arg-type]
                try:
                    maze.walk()
                except StopIteration:
                    n_loops += 1
        return n_loops
