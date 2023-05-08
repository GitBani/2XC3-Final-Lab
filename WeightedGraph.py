from Graph import Graph
from typing import List


class WeightedGraph(Graph):
    def __init__(self):
        self.__adj = {}
        self.__weights = {}
        self.__v = 0

    def get_adj_nodes(self, node: int) -> List[int]:
        return self.__adj[node]

    def add_node(self, node: int) -> None:
        self.__adj[node] = []
        self.__v += 1

    def add_edge(self, start: int, end: int, w: float) -> None:
        if end not in self.__adj[start]:
            self.__adj[start].append(end)
        self.__weights[(start, end)] = w

    def get_num_nodes(self) -> int:
        return self.__v

    def w(self, node1: int, node2: int) -> float:
        if node2 in self.__adj[node1]:
            return self.__weights[(node1, node2)]
