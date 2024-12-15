from advent_of_code_2024.array import StrArray2D
from advent_of_code_2024.data_loaders import load_file_as_array, load_file_as_string
from advent_of_code_2024.grid_location import GridLocation


class Warehouse:
    def __init__(self, moves_file: str, warehouse_file: str) -> None:
        self.array = StrArray2D(load_file_as_array(warehouse_file))
        self.robot_moves = load_file_as_string(moves_file)
        self.robot_position = self.array.find("@")[0]

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

    def score_gps(self) -> int:
        self.apply_moves()
        return sum(self.score_location(loc) for loc in self.array.find("O"))

    def score_location(self, position: GridLocation) -> int:
        return 100 * position.pos_0 + position.pos_1

    def apply_moves(self) -> None:
        for move in self.robot_moves:
            next_pos = self.move(self.robot_position, move)
            match self.array.get(next_pos):
                case "#":
                    # Wall
                    continue
                case ".":
                    # Empty space
                    self.array.set(self.robot_position, ".")
                    self.array.set(next_pos, "@")
                    self.robot_position = next_pos
                case "O":
                    # Box
                    next_check_pos = self.move(next_pos, move)
                    moveable = False
                    while True:
                        match self.array.get(next_check_pos):
                            case "#":
                                # Wall
                                break
                            case "O":
                                # Box
                                next_check_pos = self.move(next_check_pos, move)
                            case ".":
                                # Empty space
                                moveable = True
                                break
                    if moveable:
                        self.array.set(self.robot_position, ".")
                        self.array.set(next_pos, "@")
                        self.array.set(next_check_pos, "O")
                        self.robot_position = next_pos
