import heapq

def prims(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)] 

    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)
        if current not in visited:
            visited.add(current)
            if parent is not None:
                mst.append((parent, current, weight))
            for neighbor, edge_weight in graph[current].items():
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor, current))
    
    return mst

graph = {}
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    u, v, w = input("Enter the edge (format: u v w): ").split()
    w = int(w)
    if u not in graph:
        graph[u] = {}
    if v not in graph:
        graph[v] = {}
    graph[u][v] = w
    graph[v][u] = w

start = input("Enter the start node: ")

mst = prims(graph, start)

print("\nMinimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} - {v}: {weight}")
