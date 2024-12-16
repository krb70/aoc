import sys as S, pathlib as P, itertools as I, types
from collections import deque 
R, C, NS, T = range, complex, types.SimpleNamespace, -1j
_ = P.Path((S.argv+['d16.txt'])[1]).read_text().strip().split('\n')
G={C(x,y):c for x,y in I.product(R(len(_)),R(len(_[0]))) if (c:=_[x][y])!='#'}  
S=next((p for p,v in G.items() if v=='S'))

def bfs():
    res, seen, q = [], {}, deque([(0, 1j, [S], {S}, S)])
    while q:
        # track route points in sequence and in a set for speed
        cst, d, rt, s, p = q.popleft()
        if (done:=G[p]=='E'): res.append(NS(cost=cst, rt=rt))
        if done or seen.get((p,d),cst) < cst: continue
        seen[p,d] = cst
        for nd in (d*T**k for k in (1,3,4)): # right, left, forward
            if (n:=p+nd) in G and n not in s:
                np,ra,ca = d==nd and (n,[n],1) or (p,[],1000)
                q.append((cst+ca,nd,rt+ra,s|set(ra),np))
    return res

paths = bfs()
print(best:=min(p.cost for p in paths))
print(len({pt for p in filter(lambda x:x.cost==best, paths) for pt in p.rt}))
