from itertools import combinations

import numpy as np

from advent_of_code_2024.data_loaders import load_file_as_array
from advent_of_code_2024.grid_location import GridLocation


class AntennaSet:
    def __init__(
        self, name: str, positions: list[GridLocation], size: tuple[int, int]
    ) -> None:
        self.name = name
        self.positions = positions
        self.max_0 = size[0] - 1
        self.max_1 = size[1] - 1

    def antinodes(
        self, first_harmonic: int = 1, last_harmonic: int = 2
    ) -> set[GridLocation]:
        antinodes = set()
        for position_pair in combinations(self.positions, 2):
            p0_to_p1 = position_pair[1] - position_pair[0]
            # First add all harmonics subtracting from p0
            for idx_harmonic in range(first_harmonic, last_harmonic):
                antinode = position_pair[0] - idx_harmonic * p0_to_p1
                if antinode.in_bounds(self.max_0, self.max_1):
                    antinodes.add(antinode)
                else:
                    break
            # Then add all harmonics adding to p1
            for idx_harmonic in range(first_harmonic, last_harmonic):
                antinode = position_pair[1] + idx_harmonic * p0_to_p1
                if antinode.in_bounds(self.max_0, self.max_1):
                    antinodes.add(antinode)
                else:
                    break
        return antinodes


def load_antenna_sets(filename: str) -> list[AntennaSet]:
    array = load_file_as_array(filename)
    shape = (array.shape[0], array.shape[1])
    output = []
    for identifier in np.unique(array):
        if identifier == ".":
            continue
        locations = [GridLocation(loc) for loc in np.argwhere(array == identifier)]
        output.append(AntennaSet(identifier, locations, shape))
    return output
