import final_project_part1 as fp
import csv
from timeit import default_timer
from matplotlib import pyplot as plt
import numpy as np

# BUILDING
london = fp.DirectedWeightedGraph()
h, lines = {}, {}


# add nodes to graph and building heuristic
with open('london_stations.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    for row in reader:
        london.add_node(int(row[0]))
        h[int(row[0])] = (float(row[2]), float(row[1]))


# add edges
with open('london_connections.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    for row in reader:
        v1 = int(row[0])
        v2 = int(row[1])
        d = fp.distance(h, v1, v2)
        if row[2] in lines:
            lines[row[2]].append((v1, v2))
            lines[row[2]].append((v2, v1))
        else:
            lines[row[2]] = [(v1, v2)]
            lines[row[2]] = [(v2, v1)]
        london.add_edge(v1, v2, d)
        london.add_edge(v2, v1, d)


# TIMES
# with open('times.csv', 'w', newline='') as f:
#     writer = csv.writer(f, delimiter=',')
#     writer.writerow(["station 1", "station 2", "Dijkstra's time", "A Star's time", "Number of lines Taken"])
#     for v1 in london.adj:
#         print(v1)
#         for v2 in london.adj:
#             start_d = default_timer()
#             x = fp.dijkstra_(london, v1, v2)
#             end_d = default_timer()
#
#             start_a = default_timer()
#             pred = fp.a_star_(london, v1, v2, h)
#             end_a = default_timer()
#
#             path = fp.get_path(pred, v1, v2)
#             lines_used = set()
#             for i in range(len(path) - 1):
#                 for line in lines:
#                     if (path[i], path[i+1]) in lines[line]:
#                         lines_used.add(line)
#                         break
#             writer.writerow([str(v1), str(v2), str(end_d - start_d), str(end_a - start_a), len(lines_used)])


def plot_results():
    width = 0.4
    cases = ["Same Line", "Adjacent Lines", "Several transfers"]
    dijkstra, a_star = [], []

    dijkstra.append(sum(d_times_same_line) / len(d_times_same_line))
    a_star.append(sum(a_times_same_line) / len(a_times_same_line))

    dijkstra.append(sum(d_times_adj_line) / len(d_times_adj_line))
    a_star.append(sum(a_times_adj_line) / len(a_times_adj_line))

    dijkstra.append(sum(d_times_else) / len(d_times_else))
    a_star.append(sum(a_times_else) / len(a_times_else))

    values = np.arange(len(cases))
    plt.bar(values, dijkstra, width, label='Dijkstra')
    plt.bar(values+width, a_star, width, label='A Star')
    plt.legend()
    plt.xticks(values + width / 2, cases)
    plt.title("Dijkstra's algorithm vs A Star")
    plt.xlabel("Cases")
    plt.ylabel("Time (seconds)")
    plt.show()


if __name__ == '__main__':
    # PLOTTING RESULTS
    d_times_same_line = []
    a_times_same_line = []

    d_times_adj_line = []
    a_times_adj_line = []

    d_times_else = []
    a_times_else = []

    with open("times.csv", 'r') as t:
        time_reader = csv.reader(t, delimiter=',')
        next(time_reader)
        for row in time_reader:
            if row[4] == '1':
                d_times_same_line.append(float(row[2]))
                a_times_same_line.append(float(row[3]))
            elif row[4] == '2':
                d_times_adj_line.append(float(row[2]))
                a_times_adj_line.append(float(row[3]))
            else:
                d_times_else.append(float(row[2]))
                a_times_else.append(float(row[3]))
    plot_results()
