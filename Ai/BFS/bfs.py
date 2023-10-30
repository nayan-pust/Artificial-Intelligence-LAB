# Define a graph as an adjacency list
# graph = {
#     0: [1, 2,3],
#     1: [2,0],
#     2: [1, 4], 
#     3: [0],
#     4: [2] 
# }
graph = {
    'A': ['B','C'],
    'B': [ 'D'],
    'C': ['A', 'D','G'],
    'D': ['C','B','E','F'],
    'E':['D'],
    'F':['D'],
    'G':['C']
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
starting_vertex = 'A'
bfs(graph, starting_vertex)
# bfs( graph, 0)



import networkx as nx
import matplotlib.pyplot as plt

# # Define a graph as an adjacency list
# # graph = {
# #     0: [1, 2, 3],
# #     1: [2, 0],
# #     2: [1, 4],
# #     3: [0],
# #     4: [2]
# # }
# graph = {
#     1: [2,3],
    
#     2: [ 4],
#     3: [1, 4,7],
#     4: [5,6]
# }

# # Visualize the graph
G = nx.Graph(graph)
pos = nx.spring_layout(G, seed=42)  # Set a seed for reproducibility
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=12, font_weight='bold')
plt.title("Graph Visualization")
plt.show()


# Algorithm: Breadth-First Search (BFS)

# Input: Graph G represented as an adjacency list, starting vertex start.

# Initialize:

# Create an empty queue queue.
# Create an empty list visited to store visited vertices.
# Enqueue Start Vertex:

# Enqueue the start vertex into the queue.
# BFS Traversal:

# While the queue is not empty:
# Dequeue a vertex current from the queue.
# If current is not in visited:
# Mark current as visited by adding it to the visited list.
# Process current (print it or perform any other operation as needed).
# Enqueue all adjacent vertices of current that are not already visited into the queue.
# Output:

# The BFS traversal sequence is stored in the visited list.