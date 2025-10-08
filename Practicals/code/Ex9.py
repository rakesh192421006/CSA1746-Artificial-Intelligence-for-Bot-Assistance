from itertools import permutations

def tsp(graph, start=0):
    n = len(graph)
    vertices = list(range(n))
    vertices.remove(start)
    min_cost = float('inf')
    best_path = []
    for perm in permutations(vertices):
        cost = 0
        k = start
        for j in perm:
            cost += graph[k][j]
            k = j
        cost += graph[k][start]
        if cost < min_cost:
            min_cost = cost
            best_path = [start]+list(perm)+[start]
    return best_path, min_cost

graph = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
path, cost = tsp(graph)
print("Best Path:", path)
print("Minimum Cost:", cost)
