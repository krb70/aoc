import sys, re
from collections import deque
from itertools import product
from pprint import pprint

lines = open(sys.argv[1]).readlines()
g = {}
r = {}
for ln in lines:
    m = re.search(r'(..) has flow rate=(\d+).*valve(s?) (.*)', ln)
    vp = int(m.group(2))
    if vp:
        r[m.group(1)] = vp 
    g[m.group(1)] = set(x.strip() for x in m.group(4).split(','))

print(len(r))

def best(g, r, n, ddt):
    q = deque([('AA', 'AA', 1, 0, set())])
    opt = 0    
    v = {}
    ts = set()

    
    while q:
        loc, frm, t, ttl, opened = q.popleft() 
        if v.get((t, loc), -1) >= ttl: 
            continue
        v[t, loc] = ttl 

        if t == ddt:
            opt = max(opt, ttl)
            continue

        if loc in r and loc not in opened:
            newo = opened | set((loc,))
            ns = ttl + sum(r[loc] for loc in newo)
            nxt = (loc, frm, t+1, ns, newo)
            q.append(nxt)

        ns = ttl + sum(r.get(loc, 0) for loc in opened)
        for d in g[loc]:
            if d == frm and loc not in opened: continue
            nxt = (d, loc, t+1, ns, set(opened))
            q.append(nxt)

    return opt

print(best(g, r, 1, 30))

