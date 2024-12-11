from collections.abc import Sequence
from itertools import combinations

import numpy as np

from .data_loaders import load_file_as_array


class AntennaLocation:
    def __init__(self, location: Sequence[int]) -> None:
        self.pos_0 = int(location[0])
        self.pos_1 = int(location[1])

    @property
    def __id(self) -> tuple[int, int]:
        return (self.pos_0, self.pos_1)

    def __add__(self, other: "AntennaLocation") -> "AntennaLocation":
        return AntennaLocation([self.pos_0 + other.pos_0, self.pos_1 + other.pos_1])

    def __sub__(self, other: "AntennaLocation") -> "AntennaLocation":
        return AntennaLocation([self.pos_0 - other.pos_0, self.pos_1 - other.pos_1])

    def __rmul__(self, other: object) -> "AntennaLocation":
        if not isinstance(other, int):
            raise NotImplementedError
        return AntennaLocation([self.pos_0 * other, self.pos_1 * other])

    def __mul__(self, other: object) -> "AntennaLocation":
        return self.__rmul__(other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, AntennaLocation):
            return False
        if self.__id == other.__id:
            return True
        return False

    def __hash__(self) -> int:
        return hash(self.__id)

    def in_bounds(self, max_0: int, max_1: int) -> bool:
        return (0 <= self.pos_0 <= max_0) and (0 <= self.pos_1 <= max_1)


class AntennaSet:
    def __init__(
        self, name: str, positions: list[AntennaLocation], size: tuple[int, int]
    ) -> None:
        self.name = name
        self.positions = positions
        self.max_0 = size[0] - 1
        self.max_1 = size[1] - 1

    def antinodes(
        self, first_harmonic: int = 1, last_harmonic: int = 2
    ) -> set[AntennaLocation]:
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
        locations = [AntennaLocation(loc) for loc in np.argwhere(array == identifier)]
        output.append(AntennaSet(identifier, locations, shape))
    return output