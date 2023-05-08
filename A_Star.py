from SPAlgorithm import SPAlgorithm
import final_project_part1 as fp
from experiment2 import h


class A_Star(SPAlgorithm):
    def calc_sp(self, graph, source: int, dest: int) -> float:
        return fp.a_star_(graph, source, dest, h)
