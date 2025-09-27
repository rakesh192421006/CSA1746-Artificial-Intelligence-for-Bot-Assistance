def solve(n=8):
    cols=set(); pos=[]; res=[]
    def back(r):
        if r==n: res.append(pos.copy()); return
        for c in range(n):
            if c in cols or any(abs(r-r2)==abs(c-c2) for r2,c2 in enumerate(pos)): continue
            cols.add(c); pos.append(c); back(r+1); pos.pop(); cols.remove(c)
    back(0); return res
print(len(solve(8)), "solutions; first:", solve(8)[0])
