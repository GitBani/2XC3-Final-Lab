from SPAlgorithm import SPAlgorithm
from Graph import Graph
from Dijkstra import Dijkstra
from experiment2 import london


class ShortPathFinder:
    def __init__(self, graph: Graph = None, algorithm: SPAlgorithm = None):
        self.__graph = graph
        self.__algorithm = algorithm

    def calc_short_path(self, source: int, dest: int) -> float:
        return self.__algorithm.calc_sp(self.__graph, source, dest)

    def set_graph(self, graph: Graph):
        self.__graph = graph

    def set_algorithm(self, algorithm: SPAlgorithm):
        self.__algorithm = algorithm
