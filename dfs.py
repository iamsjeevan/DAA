def dfs(graph, source, visited=None):
    if visited is None:
        visited = set()
    
    print(source, end=' ')
    visited.add(source)
    
    for neighbor in graph[source]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {}
num_nodes = int(input("Enter the number of nodes: "))

for _ in range(num_nodes):
    node = input("Enter the node: ")
    neighbors = input(f"Enter the neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

source = input("Enter the source node: ")

print("\nSource node", source, "using DFS:")
dfs(graph, source)
print("\n")
