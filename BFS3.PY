import networkx as nx
import matplotlib.pyplot as plt

# Graph data
graph = {
    'A': ['C', 'B', 'E'],
    'B': ['E', 'D'],
    'C': ['F', 'G'],
    'D': ['H', 'L'],
    'E': ['I', 'J'],
    'F': ['K'],
    'G': ['K'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': []
}

# BFS function to find the shortest path
def bfs_shortest_path(graph, start, goal):
    path = {}
    queue = [start]
    path[start] = [start]

    while queue:
        current_node = queue.pop(0)
        
        if current_node == goal:
            return path[current_node]  # Return the path to the goal node

        for neighbor in graph[current_node]:
            if neighbor not in path:
                path[neighbor] = path[current_node] + [neighbor]
                queue.append(neighbor)
    
    return None

# Find the best route from A to L
start_node = 'A'
end_node = 'L'
route = bfs_shortest_path(graph, start_node, end_node)

# Create a directed graph using networkx
G = nx.DiGraph()

# Add edges to the graph
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Create a layout for the nodes
pos = nx.spring_layout(G)

# Draw the full graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=15, font_weight='bold', arrowsize=20)

# If a path was found, highlight the path
if route:
    # Draw the edges and nodes of the path in red
    path_edges = list(zip(route, route[1:]))  # Create a list of edges in the path
    nx.draw_networkx_nodes(G, pos, nodelist=route, node_color='lightgreen', node_size=3000)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
    print(f"The best route from {start_node} to {end_node} is: {' -> '.join(route)}")
else:
    print(f"No route found from {start_node} to {end_node}")

# Show the plot
plt.title(f'Shortest Path from {start_node} to {end_node}', size=20)
plt.show()
