from bisect import bisect_left
from typing import cast

from advent_of_code_2024.data_loaders import load_file_as_lines
from advent_of_code_2024.graph import Graph, Node
from advent_of_code_2024.grid_location import GridLocation


class PushdownNode(Node):
    def __init__(self, location: GridLocation) -> None:
        super().__init__(value=location)

    def key(self) -> tuple[int, int]:
        return self.location.as_tuple()

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, PushdownNode):
            raise NotImplementedError
        return self.location < other.location

    @property
    def location(self) -> GridLocation:
        return cast(GridLocation, self.value)

    def neighbours(self) -> list["PushdownNode"]:
        return [
            PushdownNode(self.location.north()),
            PushdownNode(self.location.east()),
            PushdownNode(self.location.south()),
            PushdownNode(self.location.west()),
        ]


class PushdownMaze:
    def __init__(self, filename: str, coordinate_max: int) -> None:
        self.blocks = [
            GridLocation(line.strip().split(","))
            for line in load_file_as_lines(filename)
        ]
        self.size = coordinate_max
        self.start_node = PushdownNode(GridLocation((0, 0)))
        self.end_node = PushdownNode(GridLocation((coordinate_max, coordinate_max)))

    def build_graph(self, n_blocks: int) -> Graph:
        graph = Graph()
        blocks = self.blocks[:n_blocks]
        for iy in range(self.size + 1):
            for ix in range(self.size + 1):
                node = PushdownNode(GridLocation((iy, ix)))
                for neighbour in node.neighbours():
                    if (
                        neighbour.location not in blocks
                        and neighbour.location.in_bounds(self.size, self.size)
                    ):
                        graph.add_edge(node, neighbour, 1)
        return graph

    def first_blocked_path(self) -> tuple[int, int]:
        max_n_blocks = len(self.blocks)
        return self.blocks[
            bisect_left(
                range(max_n_blocks),
                True,  # noqa: FBT003
                key=lambda n_blocks: self.path_blocked(n_blocks),
            )
            - 1
        ].as_tuple()

    def path_blocked(self, n_blocks: int) -> bool:
        try:
            self.shortest_path(n_blocks)
            return False
        except OverflowError:
            return True

    def shortest_path(self, n_blocks: int) -> int:
        graph = self.build_graph(n_blocks)
        return int(graph.dijkstra(self.start_node).get(self.end_node, float("inf")))
