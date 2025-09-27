from collections import deque
def water(a,b,target):
    start=(0,0); q=deque([start]); seen={start:None}
    while q:
        x,y=q.popleft()
        if x==target or y==target: 
            path=[]; s=(x,y)
            while s: path.append(s); s=seen[s]
            return list(reversed(path))
        states={ (a,y),(x,b),(0,y),(x,0),
                 (x-min(x,b-y),y+min(x,b-y)),(x+min(y,a-x),y-min(y,a-x)) }
        for s in states:
            if s not in seen: seen[s]= (x,y); q.append(s)
    return None
print(water(4,3,2))
