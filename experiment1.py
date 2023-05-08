import final_project_part1 as fp
from matplotlib import pyplot as plt
from random import randint

RUNS = 5
MAX_EDGE_WEIGHT = 100

# Value of K Experiment

V1 = 50


def k_exp():
    d_diffs = []
    b_diffs = []
    for k in range(1, V1):
        total_diff_d = 0
        total_diff_b = 0
        for _ in range(RUNS):
            g = fp.create_random_complete_graph(V1, MAX_EDGE_WEIGHT)
            total_diff_d += fp.total_dist(fp.dijkstra_approx(g, 0, k)) - fp.total_dist(fp.dijkstra(g, 0))
            total_diff_b += fp.total_dist(fp.bellman_ford_approx(g, 0, k)) - fp.total_dist(fp.bellman_ford(g, 0))
        d_diffs.append(total_diff_d / RUNS)
        b_diffs.append(total_diff_b / RUNS)
    return d_diffs, b_diffs


def graph_k():
    d, b = k_exp()
    x = [i for i in range(1, V1)]
    plt.title('Approximation Accuracy vs Number of Relaxations')
    plt.xlabel('Number of relaxations')
    plt.ylabel('Difference between Approximation and Original')
    plt.plot(x, d)
    plt.plot(x, b)
    plt.legend(['Dijkstra Approximation', 'Bellman Ford Approximation'])
    plt.show()


# Number of nodes

K2 = 5
V_max = 50


def v_exp():
    d_diffs = []
    b_diffs = []
    for v in range(1, V_max):
        total_diff_d = 0
        total_diff_b = 0
        for _ in range(RUNS):
            g = fp.create_random_complete_graph(v, MAX_EDGE_WEIGHT)
            total_diff_d += fp.total_dist(fp.dijkstra_approx(g, 0, K2)) - fp.total_dist(fp.dijkstra(g, 0))
            total_diff_b += fp.total_dist(fp.bellman_ford_approx(g, 0, K2)) - fp.total_dist(fp.bellman_ford(g, 0))
        d_diffs.append(total_diff_d / RUNS)
        b_diffs.append(total_diff_b / RUNS)
    return d_diffs, b_diffs


def graph_v():
    d, b = v_exp()
    x = [i for i in range(1, V_max)]
    plt.title('Approximation Accuracy vs Number of Vertices')
    plt.xlabel('Number of vertices')
    plt.ylabel('Difference between Approximation and Original')
    plt.plot(x, d)
    plt.plot(x, b)
    plt.legend(['Dijkstra Approximation', 'Bellman Ford Approximation'])
    plt.show()


# Graph Density


def max_num_of_edges(n):
    return n * (n - 1)


def create_random_graph(num_nodes, num_edges):
    g = fp.DirectedWeightedGraph()

    for node in range(num_nodes):
        g.add_node(node)

    for node in range(num_nodes - 1):
        g.add_edge(node, node + 1, randint(1, MAX_EDGE_WEIGHT))

    num_edges -= num_nodes - 1

    for i in range(min(num_edges, max_num_of_edges(num_nodes))):
        u = randint(0, num_nodes - 1)
        v = randint(0, num_nodes - 1)

        while g.are_connected(u, v) or u == v:
            u = randint(0, num_nodes - 1)
            v = randint(0, num_nodes - 1)

        g.add_edge(u, v, randint(1, MAX_EDGE_WEIGHT))

    return g


K3 = 5
V3 = 50


# suuuuuuuuper slow
def d_exp():
    d_diffs = []
    b_diffs = []
    for e in range(V3 - 1, max_num_of_edges(V3) + 1):
        print(e) # to see progress (reaches 2450)
        total_diff_d = 0
        total_diff_b = 0
        for _ in range(RUNS):
            g = create_random_graph(V3, e)
            total_diff_d += fp.total_dist(fp.dijkstra_approx(g, 0, K3)) - fp.total_dist(fp.dijkstra(g, 0))
            total_diff_b += fp.total_dist(fp.bellman_ford_approx(g, 0, K3)) - fp.total_dist(fp.bellman_ford(g, 0))
        d_diffs.append(total_diff_d / RUNS)
        b_diffs.append(total_diff_b / RUNS)
    return d_diffs, b_diffs


def graph_d():
    d, b = d_exp()
    x = [i for i in range(V3 - 1, max_num_of_edges(V3) + 1)]
    plt.title('Approximation Accuracy vs Graph Density')
    plt.xlabel('Number of edges')
    plt.ylabel('Difference between Approximation and Original')
    plt.plot(x, d)
    plt.plot(x, b)
    plt.legend(['Dijkstra Approximation', 'Bellman Ford Approximation'])
    plt.show()


if __name__ == '__main__':
    # graph_k()
    # graph_v()
    graph_d()
