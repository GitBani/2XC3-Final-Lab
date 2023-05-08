from WeightedGraph import WeightedGraph


class HeuristicGraph(WeightedGraph):
    def __init__(self, h):
        super(HeuristicGraph, self).__init__()
        self.__heuristic = h

    def get_heuristic(self):
        return self.__heuristic
