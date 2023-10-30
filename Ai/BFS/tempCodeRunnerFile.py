graph = {
    1: [2,3],
    2: [ 4],
    3: [4,7],
    4: [5,6],
    5:[4],
    6:[4],
    7:[3]
}

# Define a function to perform BFS on a graph
def bfs(graph, start):
    # Initialize a list to store the visited vertices
    visited = []
    # Initialize a queue to store the vertices to be explored
    queue = [start]
    # Loop until the queue is empty
    while queue:
        # Dequeue the first vertex from the queue
        vertex = queue.pop(0)
        # If the vertex is not visited, mark it as visited and print it
        if vertex not in visited:
            visited.append(vertex)
            print(vertex)
            # Enqueue the adjacent vertices of the current vertex that are not visited
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
    # Return the list of visited vertices
    return visited

# Call the function with a starting vertex
print("BFS Traversal starting from vertex is :")
starting_vertex = 1
bfs(graph, starting_vertex)