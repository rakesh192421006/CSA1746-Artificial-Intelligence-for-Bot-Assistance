from collections import deque

def bfs(start, goal):
    queue = deque([start])
    visited = set()
    visited.add(tuple(start))
    
    parent = {tuple(start): None}
    
    while queue:
        state = queue.popleft()
        if state == goal:
            path = []
            while state:
                path.append(state)
                state = parent[tuple(state)]
            return path[::-1]
        zero = state.index(0)
        moves = []
        if zero % 3 != 0: moves.append(zero-1)
        if zero % 3 != 2: moves.append(zero+1)
        if zero // 3 != 0: moves.append(zero-3)
        if zero // 3 != 2: moves.append(zero+3)
        for move in moves:
            new_state = state[:]
            new_state[zero], new_state[move] = new_state[move], new_state[zero]
            t_new = tuple(new_state)
            if t_new not in visited:
                visited.add(t_new)
                queue.append(new_state)
                parent[t_new] = state
    return None

start = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal = [1, 2, 3, 4, 5, 0, 6, 7, 8]
path = bfs(start, goal)
for step in path:
    print(step)
