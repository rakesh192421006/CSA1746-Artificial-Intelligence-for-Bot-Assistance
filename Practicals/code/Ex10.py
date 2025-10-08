from queue import PriorityQueue

graph = {
    'S': {'A':1,'B':4},
    'A': {'B':2,'C':5},
    'B': {'C':1,'D':3},
    'C': {'D':2},
    'D': {}
}
heuristic = {'S':7,'A':6,'B':2,'C':1,'D':0}

def a_star(start, goal):
    open_set = PriorityQueue()
    open_set.put((0,start))
    g_score = {node:float('inf') for node in graph}
    g_score[start] = 0
    parent = {start:None}

    while not open_set.empty():
        _, current = open_set.get()
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]
        for neighbor in graph[current]:
            tentative_g = g_score[current]+graph[current][neighbor]
            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f = tentative_g+heuristic[neighbor]
                open_set.put((f, neighbor))
                parent[neighbor] = current

path = a_star('S','D')
print("Path:", path)
