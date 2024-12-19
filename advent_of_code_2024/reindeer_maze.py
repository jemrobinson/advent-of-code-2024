from typing import cast

from advent_of_code_2024.data_loaders import load_file_as_array
from advent_of_code_2024.graph import Graph, Node
from advent_of_code_2024.grid_location import (
    GridLocation,
    GridVector,
    grid_vectors,
)
from advent_of_code_2024.matrix import StrMatrix


class MazeNode(Node):
    def __init__(self, location: GridLocation, direction: GridVector) -> None:
        super().__init__(value=(location, direction))

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, MazeNode):
            raise NotImplementedError
        if self.location != other.location:
            return self.location < other.location
        return self.direction < other.direction

    @property
    def location(self) -> GridLocation:
        location = self.value[0]
        if not isinstance(location, GridLocation):
            raise ValueError
        return location

    @property
    def direction(self) -> GridVector:
        direction = self.value[1]
        if not isinstance(direction, GridVector):
            raise ValueError
        return direction

    def key(self) -> tuple[tuple[int, int], tuple[int, int]]:
        return (self.location.as_tuple(), self.direction.as_tuple())

    def neighbours(self) -> list[tuple[int, "MazeNode"]]:
        return [
            # Move forward
            (1, MazeNode(self.location + self.direction, self.direction)),
            # Turn clockwise
            (1000, MazeNode(self.location, self.direction.clockwise_90())),
            # Turn anticlockwise
            (1000, MazeNode(self.location, self.direction.anticlockwise_90())),
        ]

    def reverse(self) -> "MazeNode":
        return MazeNode(self.location, self.direction.clockwise_90().clockwise_90())


class ReindeerMaze:
    def __init__(self, filename: str) -> None:
        self.array = StrMatrix(load_file_as_array(filename))
        self.directions = grid_vectors.values()
        self.start = self.array.find("S")[0]
        self.start_node = MazeNode(self.start, grid_vectors["east"])
        self.end = self.array.find("E")[0]
        self.end_nodes = [
            MazeNode(self.end, direction) for direction in self.directions
        ]
        self.graph = self.build_graph()

    def best_seats(self) -> int:
        # Get the shortest distance from the start (and shortest path)
        distances_from_start = self.graph.dijkstra(self.start_node)
        shortest_path = self.min_distance_to_end(distances_from_start)
        # Get distances from any end-state node
        distances_from_any_end_state_node = [
            self.graph.dijkstra(end_node) for end_node in self.end_nodes
        ]
        # Get shortest distance from any end-state node
        # N.B. because distances_from_any_end_state_node started at the end location,
        # we have to reverse the direction
        nodes = [cast(MazeNode, node) for node in self.graph.nodes]
        distances_from_end = {
            node.reverse(): min(
                end_dict[node] for end_dict in distances_from_any_end_state_node
            )
            for node in nodes
        }
        # Get any nodes that are on the shortest path
        nodes_on_a_shortest_path = {
            node
            for node in nodes
            if distances_from_start.get(node, float("inf"))
            + distances_from_end.get(node, float("inf"))
            == shortest_path
        }
        # Count locations belonging to these nodes
        return len({node.location for node in nodes_on_a_shortest_path})

    def build_graph(self) -> Graph:
        graph = Graph()
        for location in self.array.locations():
            for direction in self.directions:
                node = MazeNode(location, direction)
                for cost, neighbour in node.neighbours():
                    try:
                        neighbour_type = self.array.get(neighbour.location)
                    except IndexError:
                        neighbour_type = "#"
                    if neighbour_type != "#":
                        graph.add_edge(node, neighbour, cost)
        return graph

    def min_distance_to_end(self, distances: dict[Node, float]) -> int:
        return int(min(distances[end_node] for end_node in self.end_nodes))

    def shortest_path(self) -> int:
        return self.min_distance_to_end(self.graph.dijkstra(self.start_node))
