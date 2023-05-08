from abc import ABCMeta, abstractmethod
from typing import List


class Graph:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_adj_nodes(self, node: int) -> List[int]:
        pass

    @abstractmethod
    def add_node(self, node: int) -> None:
        pass

    @abstractmethod
    def add_edge(self, start: int, end: int, w: float) -> None:
        pass

    @abstractmethod
    def get_num_nodes(self) -> int:
        pass

    @abstractmethod
    def w(self, node1: int, node2: int) -> float:
        pass
