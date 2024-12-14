from functools import reduce
from operator import iadd

import numpy as np

from advent_of_code_2024.data_loaders import load_file_as_array
from advent_of_code_2024.grid_location import GridLocation


class TopographicMap:
    def __init__(self, filename: str, max_height: int = 9) -> None:
        self.array = load_file_as_array(filename).astype(int)
        self.directions = [GridLocation(t) for t in ((1, 0), (0, 1), (-1, 0), (0, -1))]
        self.max_0 = self.array.shape[0] - 1
        self.max_1 = self.array.shape[1] - 1
        self.max_height = max_height

    def find_trailheads(self) -> list[GridLocation]:
        """Find all trailheads"""
        return [
            GridLocation(position)
            for position in np.ndindex(self.array.shape)
            if self.array[position] == 0
        ]

    def rate_trailhead(self, trailhead: GridLocation) -> int:
        """Get the rating for a trailhead"""
        return len(self.unique_routes_summits(trailhead))

    def rating(self) -> int:
        """Get the total rating"""
        return sum(
            [self.rate_trailhead(trailhead) for trailhead in self.find_trailheads()]
        )

    def score_trailhead(self, trailhead: GridLocation) -> int:
        """Get the score for a trailhead"""
        return len(set(self.unique_routes_summits(trailhead)))

    def score(self) -> int:
        """Get the total score"""
        return sum(
            [self.score_trailhead(trailhead) for trailhead in self.find_trailheads()]
        )

    def unique_routes_summits(self, trailhead: GridLocation) -> list[GridLocation]:
        """Get the full list of summits at the end of a unique route"""
        positions = [trailhead]
        while self.value(positions[0]) < self.max_height:
            valid_moves = [self.valid_moves(position) for position in positions]
            positions = reduce(iadd, valid_moves, [])
        return positions

    def value(self, position: GridLocation) -> int:
        """Get the height of a location"""
        return int(self.array[position.as_tuple()])

    def valid_moves(self, start: GridLocation) -> list[GridLocation]:
        """Look for all valid moves moving upwards from start"""
        candidates = [
            c
            for c in [start + direction for direction in self.directions]
            if c.in_bounds(self.max_0, self.max_1)
        ]
        target_value = self.value(start) + 1
        return [c for c in candidates if self.array[c.as_tuple()] == target_value]
