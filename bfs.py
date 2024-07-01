def bfs(graph, source):
    visited = []
    queue = [source]

    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            print(current_node, end=' ')
            visited.append(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

graph = {}
num_nodes = int(input("Enter the number of nodes: "))

for _ in range(num_nodes):
    node = input("Enter the node: ")
    neighbors = input(f"Enter the neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

source = input("Enter the source node: ")

print("\nSource node", source, "using BFS:")
bfs(graph, source)
print("\n")
