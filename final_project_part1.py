import min_heap
import random
from math import sqrt


class DirectedWeightedGraph:

    def __init__(self):
        self.adj = {}
        self.weights = {}
        self.v = 0

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []
        self.v += 1

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)
        self.weights[(node1, node2)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return self.v

    def print_graph(self):
        print(self.adj)


def dijkstra(G, source):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.__adj.keys())

    # Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    # Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.__adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist


def dijkstra_approx(G, source, k):
    dist = {}  # Distance dictionary
    count = {}
    Q = min_heap.MinHeap([])
    nodes = list(G.__adj.keys())

    for node in nodes:
        count[node] = 0

    # Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    # Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.__adj[current_node]:
            if count[neighbour] < k:
                if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                    Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                    dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                    count[neighbour] += 1
    return dist


def bellman_ford(G, source):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    nodes = list(G.__adj.keys())

    # Initialize distances
    for node in nodes:
        dist[node] = float("inf")
    dist[source] = 0

    # Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.__adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
    return dist


def bellman_ford_approx(G, source, k):
    dist = {}  # Distance dictionary
    count = {}
    nodes = list(G.__adj.keys())

    for node in nodes:
        count[node] = 0

    # Initialize distances
    for node in nodes:
        dist[node] = float("inf")
    dist[source] = 0

    # Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.__adj[node]:
                if count[neighbour] < k:
                    if dist[neighbour] > dist[node] + G.w(node, neighbour):
                        dist[neighbour] = dist[node] + G.w(node, neighbour)
                        count[neighbour] += 1
    return dist


def total_dist(dist):
    total = 0
    for key in dist.keys():
        total += dist[key]
    return total


def create_random_complete_graph(n, upper):
    G = DirectedWeightedGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i != j:
                G.add_edge(i, j, random.randint(1, upper))
    return G


# Assumes G represents its nodes as integers 0,1,...,(n-1)
def mystery(G):
    n = G.number_of_nodes()
    d = init_d(G)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return d


def init_d(G):
    n = G.number_of_nodes()
    d = [[float("inf") for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if G.are_connected(i, j):
                d[i][j] = G.w(i, j)
        d[i][i] = 0
    return d


def get_path(pred, s, d):
    path = [d]
    while d != s:
        path.append(pred[d])
        d = pred[d]
    path.reverse()
    return path


def distance(h, p1, p2):
    return sqrt((h[p1][0] - h[p2][0]) ** 2
                + (h[p1][1] - h[p2][1]) ** 2)


def a_star(G, s, d, h):
    pred = {}
    dist = {}
    Q = min_heap.MinHeap([])
    nodes = list(G.__adj.keys())

    # Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(s, 0)
    dist[s] = 0

    # Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        if current_node == d:
            break
        for neighbour in G.__adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour) + distance(h, neighbour, d))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return pred, get_path(pred, s, d)


# for comparing times
# in Dijkstra.py
def dijkstra_(G, s, d):
    if s == d:
        return {}

    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.__adj.keys())

    # Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(s, 0)
    dist[s] = 0

    # Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        if current_node == d:
            break
        for neighbour in G.__adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist


def a_star_(G, s, d, h):
    if s == d:
        return {}

    pred = {}
    dist = {}
    Q = min_heap.MinHeap([])
    nodes = list(G.__adj.keys())

    # Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(s, 0)
    dist[s] = 0

    # Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        if current_node == d:
            break
        for neighbour in G.__adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour) + distance(h, neighbour, d))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist[d]
