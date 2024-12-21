from collections import defaultdict
from functools import lru_cache
from itertools import pairwise, product

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


class DirectionalKeypad(Keypad):
    def __init__(self) -> None:
        super().__init__(initial_state="A", lines=[".^A", "<v>"])


class NumericKeypad(Keypad):
    def __init__(self) -> None:
        super().__init__(initial_state="A", lines=["789", "456", "123", ".0A"])


class KeypadSolver:
    def __init__(self, filename: str, num_directional: int) -> None:
        self.codes = [line.strip() for line in load_file_as_lines(filename)]
        self.keypads: list[Keypad] = [NumericKeypad()]
        for _ in range(num_directional):
            self.keypads.append(DirectionalKeypad())

    @lru_cache(None)  # noqa: B019
    def n_button_presses(self, code: str, depth: int = 0) -> int:
        """Calculate minimum number of button presses recursively

        If we are at the final (human-controlled) keypad then the number of presses is the length of the code
        Otherwise, for each change from key-A -> key-B in the code
        - find the shortest paths that encode this on a directional keypad
        - for each of these paths, call this function at the next level down, to find which is the minimum
        """
        if depth == len(self.keypads):
            return len(code)
        total_presses = 0
        for c_from, c_to in pairwise(self.keypads[depth].initial_state + code):
            paths = self.keypads[depth].shortest_paths[(c_from, c_to)]
            min_presses = min(self.n_button_presses(path, depth + 1) for path in paths)
            total_presses += min_presses
        return total_presses

    def complexity(self, code: str) -> int:
        numeric_part = int("".join([c for c in code if str.isdigit(c)]))
        return self.n_button_presses(code) * numeric_part

    def total_complexity(self) -> int:
        return sum(self.complexity(code) for code in self.codes)
