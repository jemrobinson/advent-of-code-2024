from collections import defaultdict
from functools import reduce
from itertools import pairwise, product
from operator import iadd

from advent_of_code_2024.data_loaders import load_file_as_lines
from advent_of_code_2024.graph import Node
from advent_of_code_2024.grid_location import GridLocation


class ButtonNode(Node):
    def __init__(self, value: str) -> None:
        super().__init__(value=value)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, ButtonNode):
            raise NotImplementedError
        return bool(self.value < other.value)

    def heuristic(self, _: object) -> int:
        return 0


class Keypad:
    def __init__(self, initial_state: str, lines: list[str]) -> None:
        self.initial_state = initial_state

        # Get all button positions
        buttons = {
            GridLocation((idx_i, idx_j)): char_j
            for idx_i, line in enumerate(lines)
            for idx_j, char_j in enumerate(line)
            if char_j != "."
        }

        # Get all possible moves that might remain in the keypad
        n_moves_max = len(lines) + len(lines[0]) + 1
        possible_moves = {
            "".join(moves)
            for n_moves in range(n_moves_max)
            for moves in product("<>^v", repeat=n_moves)
        }

        # Get all valid paths from one button to another
        valid_paths: dict[str, dict[str, list[str]]] = defaultdict(
            lambda: defaultdict(list)
        )
        for button_pos in buttons.keys():
            for move in possible_moves:
                current_pos, valid = button_pos, True
                for char in move:
                    if char == "^":
                        current_pos = current_pos.north()
                    elif char == ">":
                        current_pos = current_pos.east()
                    elif char == "v":
                        current_pos = current_pos.south()
                    elif char == "<":
                        current_pos = current_pos.west()
                    if current_pos not in buttons:
                        valid = False
                if valid:
                    valid_paths[buttons[button_pos]][buttons[current_pos]].append(move)

        # Get all shortest paths between a pair of buttons
        self.shortest_paths = {
            (source, target): [
                p + "A" for p in paths if len(p) == min([len(p) for p in paths])
            ]
            for source, dest_dict in valid_paths.items()
            for target, paths in dest_dict.items()
        }

    def instructions(self, route: str) -> list[str]:
        instruction_sets = [""]
        for c_from, c_to in pairwise(self.initial_state + route):
            steps = self.shortest_paths[(c_from, c_to)]
            instruction_sets = [
                path + step for path in instruction_sets for step in steps
            ]
        return instruction_sets


class DirectionalKeypad(Keypad):
    def __init__(self, initial_state: str) -> None:
        super().__init__(initial_state=initial_state, lines=[".^A", "<v>"])


class NumericKeypad(Keypad):
    def __init__(self, initial_state: str) -> None:
        super().__init__(
            initial_state=initial_state, lines=["789", "456", "123", ".0A"]
        )


class KeypadSolver:
    def __init__(self, filename: str) -> None:
        self.codes = [line.strip() for line in load_file_as_lines(filename)]
        self.keypads: list[Keypad] = [
            NumericKeypad("A"),
            DirectionalKeypad("A"),
            DirectionalKeypad("A"),
        ]

    def button_presses(self, code: str) -> list[str]:
        key_presses = [code]
        for keypad in self.keypads:
            key_presses = reduce(
                iadd, [keypad.instructions(target) for target in key_presses]
            )
            min_length = min(len(kp) for kp in key_presses)
            key_presses = [kp for kp in key_presses if len(kp) == min_length]
        return key_presses

    def complexity(self, code: str) -> int:
        numeric_part = int("".join([c for c in code if str.isdigit(c)]))
        return len(self.button_presses(code)[0]) * numeric_part

    def total_complexity(self) -> int:
        return sum(self.complexity(code) for code in self.codes)
