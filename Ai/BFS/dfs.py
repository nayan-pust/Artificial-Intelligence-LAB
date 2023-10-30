graph = {
  'D' : ['E','B'],
  'B' : ['D', 'C','A'],
  'E' : ['F','D'],
  'A' : ['B'],
  'C' : ['B','F'],
  'F' : ['E','C']
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, 'C')
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
