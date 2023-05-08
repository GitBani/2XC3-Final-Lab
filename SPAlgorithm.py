from abc import ABCMeta, abstractmethod


class SPAlgorithm:
    __metaclass__ = ABCMeta

    @abstractmethod
    def calc_sp(self, graph, source: int, dest: int) -> float:
        pass
