import time
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class FibHeapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.degree = 0
        self.mark = False
        self.parent = None
        self.child = None
        self.left = self
        self.right = self

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.total_nodes = 0

    def insert(self, key, value):
        node = FibHeapNode(key, value)
        self.min_node = self._merge_with_root_list(self.min_node, node)
        self.total_nodes += 1
        return node

    def extract_min(self):
        min_node = self.min_node
        if min_node is not None:
            if min_node.child is not None:
                children = [x for x in self._iterate(min_node.child)]
                for child in children:
                    self.min_node = self._merge_with_root_list(self.min_node, child)
                    child.parent = None
            self._remove_from_root_list(min_node)
            if min_node == min_node.right:
                self.min_node = None
            else:
                self.min_node = min_node.right
                self._consolidate()
            self.total_nodes -= 1
        return min_node

    def decrease_key(self, node, new_key):
        if new_key > node.key:
            raise ValueError("new key is greater than current key")
        node.key = new_key
        parent = node.parent
        if parent is not None and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)
        if node.key < self.min_node.key:
            self.min_node = node

    def _merge_with_root_list(self, min_node, node):
        if min_node is None:
            return node
        node.left = min_node
        node.right = min_node.right
        min_node.right = node
        node.right.left = node
        return min(node, min_node, key=lambda x: x.key)

    def _remove_from_root_list(self, node):
        if node.right == node:
            return
        node.left.right = node.right
        node.right.left = node.left

    def _consolidate(self):
        A = [None] * self.total_nodes
        nodes = [w for w in self._iterate(self.min_node)]
        for w in nodes:
            x = w
            d = x.degree
            while A[d] is not None:
                y = A[d]
                if x.key > y.key:
                    x, y = y, x
                self._link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        self.min_node = None
        for a in A:
            if a is not None:
                self.min_node = self._merge_with_root_list(self.min_node, a)

    def _link(self, y, x):
        self._remove_from_root_list(y)
        y.left = y.right = y
        x.child = self._merge_with_root_list(x.child, y)
        y.parent = x
        x.degree += 1
        y.mark = False

    def _cut(self, x, y):
        self._remove_from_child_list(y, x)
        y.degree -= 1
        self.min_node = self._merge_with_root_list(self.min_node, x)
        x.parent = None
        x.mark = False

    def _remove_from_child_list(self, parent, node):
        if node.right == node:
            parent.child = None
        else:
            if parent.child == node:
                parent.child = node.right
            node.left.right = node.right
            node.right.left = node.left

    def _cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if not y.mark:
                y.mark = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)

    def _iterate(self, head):
        node = head
        stop = head
        flag = False
        while True:
            if node == stop and flag:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.right

# Standard Dijkstra's algorithm
def dijkstra_standard(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    visited = set()

    while visited != set(graph.nodes):
        current_node = min((node for node in graph if node not in visited), key=lambda node: distances[node])
        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            tentative_distance = distances[current_node] + graph[current_node][neighbor]['weight']
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance

    return distances

# Optimized Dijkstra's algorithm using a priority queue
def dijkstra_optimized(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            distance = current_distance + graph[current_node][neighbor]['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Optimized Dijkstra's algorithm using a Fibonacci heap
def dijkstra_fibonacci_heap(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    fib_heap = FibonacciHeap()
    entry_finder = {node: fib_heap.insert(distances[node], node) for node in graph}

    while fib_heap.total_nodes:
        min_node = fib_heap.extract_min()
        if min_node is None:
            break
        current_distance, current_node = min_node.key, min_node.value

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            distance = current_distance + graph[current_node][neighbor]['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                fib_heap.decrease_key(entry_finder[neighbor], distance)

    return distances

# Function to measure execution time for a given graph and algorithm
def measure_time(graph, algorithm, start_node):
    start_time = time.time()
    algorithm(graph, start_node)
    return time.time() - start_time

# Generate graphs with increasing number of nodes and measure time
node_counts = [10, 20, 40, 80, 160, 320, 640, 1280]
times_standard = []
times_optimized = []
times_fibonacci_heap = []

for count in node_counts:
    graph = nx.gnm_random_graph(count, count * 2)  # Create a random graph
    for (u, v) in graph.edges():
        graph.edges[u, v]['weight'] = 1  # Assign a weight of 1 to each edge

    start_node = 0
    times_standard.append(measure_time(graph, dijkstra_standard, start_node))
    times_optimized.append(measure_time(graph, dijkstra_optimized, start_node))
    times_fibonacci_heap.append(measure_time(graph, dijkstra_fibonacci_heap, start_node))

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(node_counts, times_standard, label='Standard Dijkstra')
plt.plot(node_counts, times_optimized, label='Optimized Dijkstra (Min-Heap)')
plt.plot(node_counts, times_fibonacci_heap, label='Optimized Dijkstra (Fibonacci Heap)')
plt.xlabel('Number of Nodes')
plt.ylabel('Time Taken (seconds)')
plt.title('Comparison of Standard and Optimized Dijkstra Algorithms')
plt.legend()
plt.grid(True)
plt.show()
