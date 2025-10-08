from collections import deque

def water_jug(a, b, target):
    queue = deque([(0,0)])
    visited = set((0,0))
    while queue:
        x, y = queue.popleft()
        if x == target or y == target:
            return True
        states = set()
        states.add((a, y))
        states.add((x, b))
        states.add((0, y))
        states.add((x, 0))
        pour_a = min(x, b-y)
        states.add((x-pour_a, y+pour_a))
        pour_b = min(y, a-x)
        states.add((x+pour_b, y-pour_b))
        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
    return False

print(water_jug(4,3,2))
