from typing import cast

from advent_of_code_2024.data_loaders import load_file_as_array
from advent_of_code_2024.graph import Graph, Node
from advent_of_code_2024.grid_location import GridLocation
from advent_of_code_2024.matrix import StrMatrix


class RaceConditionNode(Node):
    def __init__(self, location: GridLocation) -> None:
        super().__init__(value=location)

    def key(self) -> tuple[int, int]:
        return self.location.as_tuple()

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, RaceConditionNode):
            raise NotImplementedError
        return self.location < other.location

    @property
    def location(self) -> GridLocation:
        return cast(GridLocation, self.value)

    def manhattan(self, other: "RaceConditionNode") -> int:
        return self.location.manhattan(other.location)

    def neighbours(self) -> list["RaceConditionNode"]:
        return [
            RaceConditionNode(self.location.north()),
            RaceConditionNode(self.location.east()),
            RaceConditionNode(self.location.south()),
            RaceConditionNode(self.location.west()),
        ]


class RaceConditionMaze:
    def __init__(self, filename: str) -> None:
        self.array = StrMatrix(load_file_as_array(filename))
        self.start_node = RaceConditionNode(self.array.find("S")[0])
        self.end_node = RaceConditionNode(self.array.find("E")[0])
        self.graph = self.build_graph()

    def build_graph(self) -> Graph:
        graph = Graph()
        for location in self.array.locations():
            node = RaceConditionNode(location)
            for neighbour in node.neighbours():
                try:
                    neighbour_type = self.array.get(neighbour.location)
                except IndexError:
                    neighbour_type = "#"
                if neighbour_type != "#":
                    graph.add_edge(node, neighbour, 1)
        return graph

    def n_cheats(self, n_picoseconds_disabled: int, minimum_time_saved: int) -> int:
        distances = self.finite_node_distances()
        n_cheats = 0
        for node_1, d_from_start_1 in distances.items():
            for node_2, d_from_start_2 in distances.items():
                d_nodes = node_1.manhattan(node_2)
                if d_nodes <= n_picoseconds_disabled:
                    if d_from_start_2 - d_from_start_1 - d_nodes >= minimum_time_saved:
                        n_cheats += 1
        return n_cheats

    def finite_node_distances(self) -> dict[RaceConditionNode, int]:
        return {
            cast(RaceConditionNode, k): int(v)
            for k, v in self.graph.dijkstra(self.start_node).items()
            if v != float("inf")
        }
