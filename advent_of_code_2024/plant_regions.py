import numpy as np

from advent_of_code_2024.data_loaders import load_file_as_array
from advent_of_code_2024.grid_location import GridLocation
from advent_of_code_2024.matrix import StrMatrix


class Region:
    def __init__(self, name: str):
        self.name = name
        self.locations: list[GridLocation] = []

    def __str__(self) -> str:
        return f"Region(name={self.name}, area={self.area}, perimeter={self.perimeter}, sides={self.sides})"

    @property
    def area(self) -> int:
        return len(self.locations)

    @property
    def perimeter(self) -> int:
        num_adjacent_edges = sum(
            [
                location_0.adjacent(location_1)
                for location_0 in self.locations
                for location_1 in self.locations
            ]
        )
        return 4 * len(self.locations) - num_adjacent_edges

    @property
    def price(self) -> int:
        return self.area * self.perimeter

    @property
    def price_discounted(self) -> int:
        return self.area * self.sides

    @property
    def sides(self) -> int:
        """We count the number of corners, which is equivalent to the number of sides"""
        return sum(self.corners(location) for location in self.locations)

    def corners(self, location: GridLocation) -> int:
        # Check for neighbours in all compass directions
        has_north = location.north() in self.locations
        has_northeast = location.northeast() in self.locations
        has_east = location.east() in self.locations
        has_southeast = location.southeast() in self.locations
        has_south = location.south() in self.locations
        has_southwest = location.southwest() in self.locations
        has_west = location.west() in self.locations
        has_northwest = location.northwest() in self.locations
        # Number of direct neighbours
        n_neighbours = sum([has_north, has_east, has_south, has_west])
        n_filled_diagonals = (
            (has_north and has_east and has_northeast)
            + (has_south and has_east and has_southeast)
            + (has_south and has_west and has_southwest)
            + (has_north and has_west and has_northwest)
        )
        # No neighbours
        if n_neighbours == 0:
            return 4
        # One neighbour
        if n_neighbours == 1:
            return 2
        # Two neighbours
        if n_neighbours == 2:  # noqa: PLR2004
            # ... in a straight line
            if (has_north and has_south) or (has_east and has_west):
                return 0
            # ... in an L-shape: we need to check the inside diagonal
            else:
                return 2 - n_filled_diagonals
        # Three neighbours in a T-shape: we need to check the inside diagonals
        if n_neighbours == 3:  # noqa: PLR2004
            return 2 - n_filled_diagonals
        # Four neighbours in a +: we need to check the inside diagonals
        return 4 - n_filled_diagonals


class GardenPlot:
    def __init__(self, filename: str) -> None:
        self.array = StrMatrix(load_file_as_array(filename))
        self.plant_types = [str(char) for char in np.unique(self.array.array)]
        self.directions = [GridLocation(t) for t in ((1, 0), (0, 1), (-1, 0), (0, -1))]

    def build_region(self, location: GridLocation) -> Region:
        region = Region(self.array.get(location))
        location_queue = [location]
        while location_queue:
            # Skip the current location if it does not match the region's plant type
            current_location = location_queue.pop(0)
            if self.array.get(current_location) != region.name:
                continue
            # Otherwise add it to the region and add its neighbours to the queue
            region.locations.append(current_location)
            location_queue += self.get_neighbours(current_location)
            # Mark this location as visited
            self.array.set(current_location, ".")
        return region

    def find_regions(self) -> list[Region]:
        regions = []
        for location in self.array.locations():
            if self.array.get(location) in self.plant_types:
                regions.append(self.build_region(location))
        return regions

    def get_neighbours(self, location: GridLocation) -> list[GridLocation]:
        return [
            loc
            for loc in [location + direction for direction in self.directions]
            if self.array.contains(loc)
        ]

    def price(self) -> int:
        return sum([region.price for region in self.find_regions()])

    def price_discounted(self) -> int:
        return sum([region.price_discounted for region in self.find_regions()])
