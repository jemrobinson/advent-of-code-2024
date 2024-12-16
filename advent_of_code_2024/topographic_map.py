from functools import reduce
from operator import iadd

from advent_of_code_2024.data_loaders import load_file_as_array
from advent_of_code_2024.grid_location import GridLocation
from advent_of_code_2024.matrix import IntMatrix


class TopographicMap:
    def __init__(self, filename: str, max_height: int = 9) -> None:
        self.matrix = IntMatrix(load_file_as_array(filename).astype(int))
        self.directions = [GridLocation(t) for t in ((1, 0), (0, 1), (-1, 0), (0, -1))]
        self.max_height = max_height

    def find_trailheads(self) -> list[GridLocation]:
        """Find all trailheads"""
        return self.matrix.find(0)

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
        while self.matrix.get(positions[0]) < self.max_height:
            valid_moves = [self.valid_moves(position) for position in positions]
            positions = reduce(iadd, valid_moves, [])
        return positions

    def valid_moves(self, start: GridLocation) -> list[GridLocation]:
        """Look for all valid moves moving upwards from start"""
        target_value = self.matrix.get(start) + 1
        return [
            candidate
            for candidate in [start + direction for direction in self.directions]
            if candidate.in_bounds(*self.matrix.bounds())
            and self.matrix.get(candidate) == target_value
        ]
