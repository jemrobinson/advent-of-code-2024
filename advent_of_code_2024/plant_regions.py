import numpy as np

from advent_of_code_2024.array import StrArray2D
from advent_of_code_2024.data_loaders import load_file_as_array
from advent_of_code_2024.grid_location import GridLocation


class Region:
    def __init__(self, name: str):
        self.name = name
        self.locations: list[GridLocation] = []

    def __str__(self) -> str:
        return f"Region(name={self.name}, area={self.area}, perimeter={self.perimeter}, price={self.price})"

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


class GardenPlot:
    def __init__(self, filename: str) -> None:
        self.array = StrArray2D(load_file_as_array(filename))
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
