import heapq
from collections.abc import Iterable
from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value

    def key(self) -> Any:
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return False
        if self.value == other.value:
            return True
        return False

    def __hash__(self) -> int:
        return hash(self.key())

    def __lt__(self, _: object) -> bool:
        raise NotImplementedError


class Graph:
    def __init__(self) -> None:
        self.graph: dict[Node, dict[Node, float]] = {}

    def add_edge(self, source: Node, target: Node, distance: float) -> None:
        if source not in self.graph:
            self.graph[source] = {}
        # print(f"Adding edge from {str(source)} to {str(target)} with cost {distance}")
        self.graph[source][target] = distance

    def dijkstra(self, start: Node) -> dict[Node, float]:
        """Implement Dijkstra's algorithm"""
        distances = {node: float("inf") for node in self.graph}
        distances[start] = 0

        # Initialise the queue of nodes to visit
        queue = [(0, start)]
        heapq.heapify(queue)

        # Initialise the set of visited nodes
        visited = set()

        # Iterate until the queue is exhausted
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if current_node in visited:
                continue
            visited.add(current_node)

            for node, distance in self.graph[current_node].items():
                candidate_distance = current_distance + distance
                # If this is the shortest distance to this node then
                # - store the distance
                # - add this to the queue
                if candidate_distance < distances[node]:
                    distances[node] = candidate_distance
                    heapq.heappush(queue, (candidate_distance, node))  # type: ignore[misc]

        # Return the distances to each node
        return distances

    def nodes(self) -> Iterable[Node]:
        return self.graph.keys()
