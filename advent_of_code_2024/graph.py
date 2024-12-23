import heapq
from collections import deque
from collections.abc import Iterable
from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value

    def key(self) -> Any:
        return self.value

    def heuristic(self, _: object) -> float:
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return False
        if self.value == other.value:
            return True
        return False

    def __hash__(self) -> int:
        return hash(self.key())

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Node):
            raise NotImplementedError
        return bool(self.value < other.value)


class Graph:
    def __init__(self) -> None:
        self.graph: dict[Node, dict[Node, float]] = {}

    @property
    def nodes(self) -> Iterable[Node]:
        return self.graph.keys()

    def add_edge(self, source: Node, target: Node, distance: float) -> None:
        if source not in self.graph:
            self.graph[source] = {}
        self.graph[source][target] = distance

    def a_star(self, start: Node, target: Node) -> tuple[list[Node], float]:
        """Implement the A* algorithm"""
        # Initialise the queue of nodes to visit
        # Priority is distance-from-start + estimated-distance-to-target
        queue = [(0, start)]
        heapq.heapify(queue)

        came_from: dict[Node, Node] = {start: start}
        distances: dict[Node, float] = {start: 0}

        while queue:
            _, current = heapq.heappop(queue)
            if current == target:
                break

            for node, distance in self.graph[current].items():
                candidate_distance = distances[current] + distance
                if node not in distances or candidate_distance < distances[node]:
                    distances[node] = candidate_distance
                    priority = candidate_distance + target.heuristic(node)
                    heapq.heappush(queue, (priority, node))  # type: ignore[misc]
                    came_from[node] = current

        # Reconstruct the path
        path: list[Node] = []
        if target in came_from:
            current = target
            while current and current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()

        return (path, distances.get(target, float("inf")))

    def bfs(self, start: Node) -> set[Node]:
        """Implement breadth-first search (no queue priority)"""
        # Initialise the queue of nodes to visit
        queue = deque([start])

        # Initialise the set of visited nodes
        visited = set()

        # Iterate until the queue is exhausted
        while queue:
            current_node = queue.popleft()
            if current_node in visited:
                continue
            visited.add(current_node)
            queue += list(self.graph[current_node].keys())

        # Return set of accessible nodes
        return visited

    def bron_kerbosch(
        self, r_nodes: set[Node], p_nodes: set[Node], x_nodes: set[Node]
    ) -> list[set[Node]]:
        """Implement the Bron-Kerbosch algorithm without pivot"""
        output = []
        if not p_nodes and not x_nodes:
            return [r_nodes]
        for node in list(p_nodes):
            neighbours = self.neighbours(node)
            output.extend(
                self.bron_kerbosch(
                    r_nodes.union({node}),
                    p_nodes.intersection(neighbours),
                    x_nodes.intersection(neighbours),
                )
            )
            p_nodes.remove(node)
            x_nodes.add(node)
        return output

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

    def maximal_cliques(self) -> list[set[Node]]:
        """Use Bron-Kerbosch to return all maximal cliques"""
        return self.bron_kerbosch(set(), set(self.nodes), set())

    def neighbours(self, node: Node) -> set[Node]:
        return set(self.graph[node].keys())
