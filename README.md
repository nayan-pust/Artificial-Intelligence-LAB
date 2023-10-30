# AI-LAB


# BFS GRAPH
![image](https://github.com/nayan-pust/AI-LAB/assets/114688354/04617374-7189-4dbb-a400-bd52e97db222)


# DFS   GRAPH
![image](https://github.com/nayan-pust/AI-LAB/assets/114688354/ed79302a-6e36-4e9c-b8a1-85f6aaf24de7)


# Travelling Salesman Graph
![image](https://github.com/nayan-pust/AI-LAB/assets/114688354/bb08ed78-0095-4733-b47f-8e0b229ea8f5)
```ruby
from sys import maxsize
from itertools import permutations

V = 4

def tsp(graph, s, city_names):
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

    # Print the visited nodes by their names
    visited_cities = [city_names[node] for node in min_path]
    print("Visited Nodes:", " -> ".join(visited_cities))

    return min_cost, min_path

graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
s = 0

# Define city names corresponding to vertices
city_names = ["City A", "City B", "City C", "City D"]

min_cost, min_path = tsp(graph, s, city_names)
print("Minimum Cost:", min_cost)
print("Minimum Path:", min_path)
```
![image](https://github.com/nayan-pust/AI-LAB/assets/114688354/290d5305-ae51-4096-b88e-9b5e92f03e8e)


# Iris Flower Classicfication 
![image](https://github.com/nayan-pust/AI-LAB/assets/114688354/71cc2b51-31ae-4547-82c8-c0e2a066857e)

# sepal length & width
The figures above show that Iris setosa has sepal length not greater than 6.0 cm and sepal width not less than 2.3 cm;
Iris versicolor has sepal length not less than 5.0 cm and sepal width not greater than 3.4 cm; 
Iris virginica has sepal length not less than 6.0 cm and sepal width not greater than 3.8 cm.



