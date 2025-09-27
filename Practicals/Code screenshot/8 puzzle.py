import heapq
goal=(1,2,3,4,5,6,7,8,0)
def man(s): return sum(abs((s.index(i)//3)-(goal.index(i)//3))+abs((s.index(i)%3)-(goal.index(i)%3)) for i in range(1,9))
def neighbors(s):
    i=s.index(0); r,c=divmod(i,3)
    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr,nc=r+dr,c+dc
        if 0<=nr<3 and 0<=nc<3:
            lst=list(s); j=nr*3+nc; lst[i],lst[j]=lst[j],lst[i]; yield tuple(lst)
def astar(start):
    pq=[(man(start),0,start,None)]; seen={}
    while pq:
        f,g,s,par=heapq.heappop(pq)
        if s in seen: continue
        seen[s]=par
        if s==goal:
            path=[] 
            while s: path.append(s); s=seen[s]
            return list(reversed(path))
        for nb in neighbors(s):
            if nb in seen: continue
            heapq.heappush(pq,(g+1+man(nb),g+1,nb,s))
start=(1,2,3,4,0,6,7,5,8)
for p in astar(start): print(p)
