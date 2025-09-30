from collections import deque
def mc():
    start=(3,3,0); goal=(0,0,1)
    moves=[(1,0),(2,0),(0,1),(0,2),(1,1)]
    q=deque([start]); pred={start:None}
    while q:
        m,c,b=q.popleft()
        if (m,c,b)==goal:
            path=[]; s=goal
            while s: path.append(s); s=pred[s]
            return list(reversed(path))
        for dm,dc in moves:
            nb=(m-dm if b==0 else m+dm, c-dc if b==0 else c+dc, 1-b)
            M,C=nb[0],nb[1]
            if 0<=M<=3 and 0<=C<=3 and (M==0 or M>=C) and (3-M==0 or 3-M>=3-C) and nb not in pred:
                pred[nb]=(m,c,b); q.append(nb)
print(mc())
