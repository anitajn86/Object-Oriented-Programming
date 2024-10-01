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

def bfs_shortest_path(graph, start, goal):
    # A dictionary to store the path that leads to each node
    path = {}
    # Initialize the queue with the starting node
    queue = [start]
    # Mark the starting node as visited (path from start to itself is just the start)
    path[start] = [start]

    while queue:
        # Dequeue a node
        current_node = queue.pop(0)
        
        # Check if we've reached the goal
        if current_node == goal:
            return path[current_node]  # Return the path to the goal node

        # Visit all neighbors
        for neighbor in graph[current_node]:
            if neighbor not in path:
                # Store the path to the neighbor by extending the current path
                path[neighbor] = path[current_node] + [neighbor]
                queue.append(neighbor)
    
    return None  # Return None if no path is found

# Find the best route from A to L
start_node = 'A'
end_node = 'L'
route = bfs_shortest_path(graph, start_node, end_node)

if route:
    print(f"The best route from {start_node} to {end_node} is: {' -> '.join(route)}")
else:
    print(f"No route found from {start_node} to {end_node}")
