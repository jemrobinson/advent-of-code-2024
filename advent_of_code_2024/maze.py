import enum

import numpy as np

from .data_loaders import load_file_as_lines

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

    def turn(self) -> None:
        self.direction = Direction((self.direction + 1) % len(Direction))


class Maze:
    def __init__(self, filename: str) -> None:
        lines = load_file_as_lines(filename)
        self.array = np.array([list(line.strip()) for line in lines])
        coords = [int(coord) for coord in np.where(self.array == "^")]
        self.guard = Guard((coords[0], coords[1]), Direction.NORTH)
        self.n_steps = 0

    def value(self, position: Position) -> str:
        return str(self.array[position[0], position[1]])

    def mark(self, position: Position, value: str) -> None:
        self.array[position[0], position[1]] = value

    def step(self) -> None:
        self.n_steps += 1
        next_position = self.guard.next_position()
        if not (
            (0 <= next_position[0] < self.array.shape[0])
            and (0 <= next_position[1] < self.array.shape[1])
        ):
            msg = "Out-of-bounds"
            raise ValueError(msg)
        match self.value(next_position):
            case "." | "x":
                self.mark(self.guard.position, "x")
                self.mark(next_position, "@")
                self.guard.position = next_position
            case "#":
                self.guard.turn()

    def walk(self) -> int:
        try:
            while True:
                self.step()
        except ValueError:
            counts = dict(zip(*np.unique(self.array, return_counts=True), strict=False))
            return int(counts["x"] + counts["@"])
