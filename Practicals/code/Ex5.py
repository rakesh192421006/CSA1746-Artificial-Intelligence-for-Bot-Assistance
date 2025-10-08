from collections import deque

def missionaries_cannibals():
    start = (3,3,1)
    goal = (0,0,0)
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}

    while queue:
        state = queue.popleft()
        m, c, b = state
        if state == goal:
            path = []
            while state:
                path.append(state)
                state = parent[state]
            return path[::-1]

        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
        for dm, dc in moves:
            if b==1:
                nm, nc = m-dm, c-dc
                nb = 0
            else:
                nm, nc = m+dm, c+dc
                nb = 1
            if 0 <= nm <= 3 and 0 <= nc <= 3:
                if (nm==0 or nm>=nc) and (3-nm==0 or 3-nm >= 3-nc):
                    new_state = (nm, nc, nb)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)
                        parent[new_state] = state

path = missionaries_cannibals()
for step in path:
    print(step)
