from sys import maxsize
from itertools import permutations

V = 4

def tsp(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    min_cost = maxsize
    min_path = []
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_cost = 0
        path = [s]
        k = s
        for j in i:
            current_cost += graph[k][j]
            path.append(j)
            k = j
        current_cost += graph[k][s]
        path.append(s)
        if current_cost < min_cost:
            min_cost = current_cost
            min_path = path
    return min_cost, min_path

graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
s = 0
min_cost, min_path = tsp(graph, s)
print("Minimum Cost:", min_cost)
print("Minimum Path:", min_path)



