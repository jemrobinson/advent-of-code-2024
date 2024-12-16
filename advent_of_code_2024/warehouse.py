import copy

import numpy as np

from advent_of_code_2024.data_loaders import (
    load_file_as_array,
    load_file_as_lines,
    load_file_as_string,
)
from advent_of_code_2024.grid_location import GridLocation
from advent_of_code_2024.matrix import StrMatrix


class Warehouse:
    def __init__(self, moves_file: str, warehouse_file: str) -> None:
        self.matrix = StrMatrix(load_file_as_array(warehouse_file))
        self.robot_moves = load_file_as_string(moves_file)
        self.robot_position = self.matrix.find("@")[0]

    @staticmethod
    def move(position: GridLocation, direction: str) -> GridLocation:
        if direction == "^":
            return position.north()
        if direction == ">":
            return position.east()
        if direction == "v":
            return position.south()
        if direction == "<":
            return position.west()
        raise ValueError

    def apply_moves(self) -> None:
        for move in self.robot_moves:
            next_robot_pos = self.move(self.robot_position, move)
            match self.matrix.get(next_robot_pos):
                # Wall
                case "#":
                    continue
                # Empty space
                case ".":
                    self.matrix.set(self.robot_position, ".")
                    self.matrix.set(next_robot_pos, "@")
                    self.robot_position = next_robot_pos
                # Box
                case "O":
                    next_check_pos = self.move(next_robot_pos, move)
                    moveable = False
                    while True:
                        match self.matrix.get(next_check_pos):
                            # Wall
                            case "#":
                                break
                            # Box
                            case "O":
                                next_check_pos = self.move(next_check_pos, move)
                            # Empty space
                            case ".":
                                moveable = True
                                break
                    if moveable:
                        self.matrix.set(self.robot_position, ".")
                        self.matrix.set(next_robot_pos, "@")
                        self.matrix.set(next_check_pos, "O")
                        self.robot_position = next_robot_pos

    def score_gps(self) -> int:
        self.apply_moves()
        return sum(self.score_location(loc) for loc in self.matrix.find("O"))

    def score_location(self, position: GridLocation) -> int:
        return 100 * position.pos_0 + position.pos_1


class LargeBox:
    def __init__(
        self, *, lhs: GridLocation | None = None, rhs: GridLocation | None = None
    ) -> None:
        if lhs:
            self.lhs = lhs
            self.rhs = lhs.east()
        elif rhs:
            self.rhs = rhs
            self.lhs = rhs.west()

    def is_moveable(self, direction: str, grid: StrMatrix) -> bool:  # noqa: PLR0911
        if direction == "^":
            # LHS
            lhs_north = self.lhs.north()
            lhs_north_value = grid.get(lhs_north)
            if lhs_north_value == "#":
                lhs_is_moveable = False
            elif lhs_north_value == ".":
                lhs_is_moveable = True
            elif lhs_north_value == "[":
                lhs_is_moveable = LargeBox(lhs=lhs_north).is_moveable(direction, grid)
            elif lhs_north_value == "]":
                lhs_is_moveable = LargeBox(rhs=lhs_north).is_moveable(direction, grid)
            # RHS
            rhs_north = self.rhs.north()
            rhs_north_value = grid.get(rhs_north)
            if rhs_north_value == "#":
                rhs_is_moveable = False
            elif rhs_north_value == ".":
                rhs_is_moveable = True
            elif rhs_north_value == "[":
                rhs_is_moveable = LargeBox(lhs=rhs_north).is_moveable(direction, grid)
            elif rhs_north_value == "]":
                rhs_is_moveable = LargeBox(rhs=rhs_north).is_moveable(direction, grid)
            return lhs_is_moveable and rhs_is_moveable
        if direction == ">":
            rhs_east = self.rhs.east()
            match grid.get(rhs_east):
                case "#":
                    return False
                case ".":
                    return True
                case "[":
                    return LargeBox(lhs=rhs_east).is_moveable(direction, grid)
                case "]":
                    msg = "There should not be a ']' to the east of this box"
                    raise ValueError(msg)
        if direction == "v":
            # LHS
            lhs_south = self.lhs.south()
            lhs_south_value = grid.get(lhs_south)
            if lhs_south_value == "#":
                lhs_is_moveable = False
            elif lhs_south_value == ".":
                lhs_is_moveable = True
            elif lhs_south_value == "[":
                lhs_is_moveable = LargeBox(lhs=lhs_south).is_moveable(direction, grid)
            elif lhs_south_value == "]":
                lhs_is_moveable = LargeBox(rhs=lhs_south).is_moveable(direction, grid)
            # RHS
            rhs_south = self.rhs.south()
            rhs_south_value = grid.get(rhs_south)
            if rhs_south_value == "#":
                rhs_is_moveable = False
            elif rhs_south_value == ".":
                rhs_is_moveable = True
            elif rhs_south_value == "[":
                rhs_is_moveable = LargeBox(lhs=rhs_south).is_moveable(direction, grid)
            elif rhs_south_value == "]":
                rhs_is_moveable = LargeBox(rhs=rhs_south).is_moveable(direction, grid)
            return lhs_is_moveable and rhs_is_moveable
        if direction == "<":
            lhs_west = self.lhs.west()
            match grid.get(lhs_west):
                case "#":
                    return False
                case ".":
                    return True
                case "]":
                    return LargeBox(rhs=lhs_west).is_moveable(direction, grid)
                case "[":
                    msg = "There should not be a '[' to the west of this box"
                    raise ValueError(msg)
        # Default case should be unreachable
        return False

    def move_recursive(self, direction: str, grid: StrMatrix) -> StrMatrix:
        output_grid = copy.deepcopy(grid)
        if direction == "^":
            lhs_north = self.lhs.north()
            rhs_north = self.rhs.north()
            # Check whether other boxes need to be moved
            lhs_north_value = grid.get(lhs_north)
            rhs_north_value = grid.get(rhs_north)
            # Box due north
            if lhs_north_value == "[" and rhs_north_value == "]":
                output_grid = LargeBox(lhs=lhs_north).move_recursive(
                    direction, output_grid
                )
            # Box north west
            else:
                if lhs_north_value == "]":
                    output_grid = LargeBox(rhs=lhs_north).move_recursive(
                        direction, output_grid
                    )
                # Box north east
                if rhs_north_value == "[":
                    output_grid = LargeBox(lhs=rhs_north).move_recursive(
                        direction, output_grid
                    )
                # Check for unexpected walls
                if lhs_north_value == "#" or rhs_north_value == "#":
                    msg = f"Attempting to move into wall: {lhs_north_value=} {rhs_north_value=}"
                    raise ValueError(msg)
            # Move this box
            output_grid.set(self.lhs, ".")
            output_grid.set(self.rhs, ".")
            output_grid.set(self.lhs.north(), "[")
            output_grid.set(self.rhs.north(), "]")
        elif direction == ">":
            rhs_east = self.rhs.east()
            # Check whether other boxes need to be moved
            rhs_east_value = grid.get(rhs_east)
            if rhs_east_value == "[":
                output_grid = LargeBox(lhs=rhs_east).move_recursive(
                    direction, output_grid
                )
            # Move this box
            output_grid.set(self.lhs, ".")
            output_grid.set(self.rhs, "[")
            output_grid.set(self.rhs.east(), "]")
        elif direction == "v":
            lhs_south = self.lhs.south()
            rhs_south = self.rhs.south()
            # Check whether other boxes need to be moved
            lhs_south_value = grid.get(lhs_south)
            rhs_south_value = grid.get(rhs_south)
            # Box due south
            if lhs_south_value == "[" and rhs_south_value == "]":
                output_grid = LargeBox(lhs=lhs_south).move_recursive(
                    direction, output_grid
                )
            # Box south west
            else:
                if lhs_south_value == "]":
                    output_grid = LargeBox(rhs=lhs_south).move_recursive(
                        direction, output_grid
                    )
                # Box south east
                if rhs_south_value == "[":
                    output_grid = LargeBox(lhs=rhs_south).move_recursive(
                        direction, output_grid
                    )
                # Check for unexpected walls
                if lhs_south_value == "#" or rhs_south_value == "#":
                    msg = f"Attempting to move into wall: {lhs_south_value=} {rhs_south_value=}"
                    raise ValueError(msg)
            # Move this box
            output_grid.set(self.lhs, ".")
            output_grid.set(self.rhs, ".")
            output_grid.set(lhs_south, "[")
            output_grid.set(rhs_south, "]")
        elif direction == "<":
            lhs_west = self.lhs.west()
            # Check whether other boxes need to be moved
            lhs_west_value = grid.get(lhs_west)
            if lhs_west_value == "]":
                output_grid = LargeBox(rhs=lhs_west).move_recursive(
                    direction, output_grid
                )
            # Move this box
            output_grid.set(lhs_west, "[")
            output_grid.set(self.lhs, "]")
            output_grid.set(self.rhs, ".")
        # Return the grid
        return output_grid


class LargeWarehouse(Warehouse):
    def __init__(self, moves_file: str, warehouse_file: str) -> None:
        super().__init__(moves_file, warehouse_file)
        self.matrix = StrMatrix(
            np.array(
                [
                    list(
                        line.strip()
                        .replace("#", "##")
                        .replace("O", "[]")
                        .replace(".", "..")
                        .replace("@", "@.")
                    )
                    for line in load_file_as_lines(warehouse_file)
                ]
            )
        )
        self.robot_position = self.matrix.find("@")[0]

    def apply_moves(self) -> None:
        for move in self.robot_moves:
            if len(self.matrix.find("[")) != len(self.matrix.find("]")):
                msg = "Invalid array"
                raise ValueError(msg)
            next_robot_pos = self.move(self.robot_position, move)
            match self.matrix.get(next_robot_pos):
                # Wall
                case "#":
                    continue
                # Empty space
                case ".":
                    self.matrix.set(self.robot_position, ".")
                    self.matrix.set(next_robot_pos, "@")
                    self.robot_position = next_robot_pos
                # Box LHS
                case "[":
                    box = LargeBox(lhs=next_robot_pos)
                    if box.is_moveable(move, self.matrix):
                        self.matrix = box.move_recursive(move, grid=self.matrix)
                        self.matrix.set(self.robot_position, ".")
                        self.matrix.set(next_robot_pos, "@")
                        self.robot_position = next_robot_pos
                # Box RHS
                case "]":
                    box = LargeBox(rhs=next_robot_pos)
                    if box.is_moveable(move, self.matrix):
                        self.matrix = box.move_recursive(move, grid=self.matrix)
                        self.matrix.set(self.robot_position, ".")
                        self.matrix.set(next_robot_pos, "@")
                        self.robot_position = next_robot_pos

    def score_gps(self) -> int:
        self.apply_moves()
        return sum(self.score_location(loc) for loc in self.matrix.find("["))
