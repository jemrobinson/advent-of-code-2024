from advent_of_code_2024.data_loaders import load_file_as_lines
from advent_of_code_2024.graph import Graph, Node


class LanParty:
    def __init__(self, filename: str) -> None:
        self.graph = Graph()
        for line in load_file_as_lines(filename):
            comp_0, comp_1 = line.strip().split("-")
            # Double up node-edges as the graph is directed
            self.graph.add_edge(Node(comp_0), Node(comp_1), 1)
            self.graph.add_edge(Node(comp_1), Node(comp_0), 1)

    def find_password(self) -> str:
        largest_cluster = max(
            self.graph.maximal_cliques(), key=lambda clique: len(clique)
        )
        return ",".join(sorted([node.value for node in largest_cluster]))

    def find_triples(self) -> set[tuple[Node, Node, Node]]:
        triples = set()
        for node_i in self.graph.nodes:
            for node_j in self.graph.neighbours(node_i):
                for node_k in self.graph.neighbours(node_j):
                    if node_i in self.graph.neighbours(node_k):
                        triples.add(tuple(sorted([node_i, node_j, node_k])))
        return triples  # type: ignore[return-value]

    def count_triples_with_ts(self) -> int:
        return sum(
            any(node.value.startswith("t") for node in triple)
            for triple in self.find_triples()
        )
