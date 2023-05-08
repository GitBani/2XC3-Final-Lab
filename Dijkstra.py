from SPAlgorithm import SPAlgorithm
import min_heap


class Dijkstra(SPAlgorithm):
    def calc_sp(self, graph, source: int, dest: int) -> float:
        if source == dest:
            return 0

        dist = {}
        queue = min_heap.MinHeap([])
        nodes = list(graph.__adj.keys())

        # Initialize priority queue/heap and distances
        for node in nodes:
            queue.insert(min_heap.Element(node, float("inf")))
            dist[node] = float("inf")
        queue.decrease_key(source, 0)
        dist[source] = 0

        # Meat of the algorithm
        while not queue.is_empty():
            current_element = queue.extract_min()
            current_node = current_element.value
            if current_node == dest:
                break
            for neighbour in graph.__adj[current_node]:
                if dist[current_node] + graph.w(current_node, neighbour) < dist[neighbour]:
                    queue.decrease_key(neighbour, dist[current_node] + graph.w(current_node, neighbour))
                    dist[neighbour] = dist[current_node] + graph.w(current_node, neighbour)
        return dist[dest]
