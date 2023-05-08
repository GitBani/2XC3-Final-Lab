import final_project_part1 as fp
from timeit import default_timer as timer
from experiment1 import create_random_graph, max_num_of_edges
from matplotlib import pyplot as plt
import numpy as np


def mystery_graph_times(dense):
    times = []
    for n in range(200):
        g = create_random_graph(n, max_num_of_edges(n) if dense else n)
        start = timer()
        fp.mystery(g)
        end = timer()
        print(n)
        times.append(end - start)
    return times


def mystery_graph_times_for_loglog(dense):
    times = []
    for n in np.logspace(1, 3, num=7, dtype=int):
        g = create_random_graph(n, max_num_of_edges(n) if dense else n)
        start = timer()
        fp.mystery(g)
        end = timer()
        print(n)
        times.append(end - start)
    return times


if __name__ == '__main__':
    min_density_times = mystery_graph_times(False)
    max_density_times = mystery_graph_times(True)

    plt.title("Mystery Algorithm Runtime")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Time (seconds)")
    plt.plot(min_density_times)
    plt.plot(max_density_times)
    plt.legend(["Minimum Density", "Maximum Density"])
    plt.show()

    # mystery depends heavily on V, not much on E, so we only test on minimum densities
    min_density_times = mystery_graph_times_for_loglog(False)
    plt.xlabel('Graph Size')
    plt.ylabel('Time')
    plt.loglog(min_density_times)
    plt.title("Mystery Algorithm Runtime")
    plt.show()
    fit = np.polyfit(np.log(np.logspace(1, 3, num=7, dtype=int)),
                     np.log(min_density_times),
                     deg=1
                     )
    print(fit[0])
