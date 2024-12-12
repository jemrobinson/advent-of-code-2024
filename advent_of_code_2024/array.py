from collections.abc import Generator

import numpy as np

from .grid_location import GridLocation


class Array2D:
    def __init__(self, array: np.ndarray) -> None:  # type: ignore[type-arg]
        self.array = array

    def contains(self, location: GridLocation) -> bool:
        valid_0 = bool(0 <= location.pos_0 < self.array.shape[0])
        valid_1 = bool(0 <= location.pos_1 < self.array.shape[1])
        return valid_0 and valid_1

    def locations(self) -> Generator[GridLocation, None, None]:
        for location in np.ndindex(self.array.shape):
            yield GridLocation(location)


class IntArray2D(Array2D):
    def get(self, location: GridLocation) -> int:
        return int(self.array[location.as_tuple()])

    def set(self, location: GridLocation, value: int) -> None:
        self.array[location.as_tuple()] = value


class StrArray2D(Array2D):
    def get(self, location: GridLocation) -> str:
        return str(self.array[location.as_tuple()])

    def set(self, location: GridLocation, value: str) -> None:
        self.array[location.as_tuple()] = value
