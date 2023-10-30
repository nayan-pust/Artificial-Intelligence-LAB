# # Define a graph as an adjacency list
# # graph = {
# #     0: [1, 2,3],
# #     1: [0, 3, 4],
# #     2: [0, 4],
# #     3: [1, 4],
# #     4: [1, 2, 3]
# # }

# graph = {
#     1: [2,3],
#     2: [ 4],
#     3: [1, 4,7],
#     4: [5,6],
#     5:[4],
#     6:[4],
#     7:[3]
# }

# # Define a function to perform DFS on a graph
# def dfs(graph, start):
#     # Initialize a list to store the visited vertices
#     visited = []
#     # Initialize a stack to store the vertices to be explored
#     stack = [start]
#     # Loop until the stack is empty
#     while stack:
#         # Pop the last vertex from the stack
#         vertex = stack.pop()
#         # If the vertex is not visited, mark it as visited and print it
#         if vertex not in visited:
#             visited.append(vertex)
#             print(vertex)
#             # Push the adjacent vertices of the current vertex that are not visited to the stack
#             for neighbor in graph[vertex]:
#                 if neighbor not in visited:
#                     stack.append(neighbor)
#     # Return the list of visited vertices
#     return visited

# # # Call the function with a starting vertex
# starting_vertex = 1
# print("DFS Traversal starting from vertex is :")
# dfs(graph, starting_vertex)


# # Define a graph as an adjacency list
# graph = {
#     0: [1, 2,3],
#     1: [2,0],
#     2: [1, 4], 
#     3: [0],
#     4: [2] 
# }

import networkx as nx
import matplotlib.pyplot as plt

graph = {
    'A': ['B','C'],
    'B': [ 'D'],
    'C': ['A', 'D','G'],
    'D': ['C','B','E','F'],
    'E':['D'],
    'F':['D'],
    'G':['C']
}

# Define a function to perform DFS on a graph
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Call the function with a starting vertex

# Call the function with a starting vertex (for example, starting from vertex 3)
starting_vertex = 'A'
print("DFS Traversal starting from vertex is :")
dfs(graph, starting_vertex)

G = nx.Graph(graph)
pos = nx.spring_layout(G, seed=42)  # Set a seed for reproducibility
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=12, font_weight='bold')
plt.title("Graph Visualization")
plt.show()

