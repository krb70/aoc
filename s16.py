import sys, re
from collections import deque, defaultdict
from itertools import product
from pprint import pprint
from functools import reduce
from operator import or_

lines = open(sys.argv[1]).readlines()
g = {}
r = {}
for ln in lines:
    m = re.search(r'(..) has flow rate=(\d+).*valve(s?) (.*)', ln)
    vp = int(m.group(2))
    if vp:
        r[m.group(1)] = vp 
    g[m.group(1)] = set(x.strip() for x in m.group(4).split(','))

def run(g, r, n, ddt):
    wp = ('AA',) * n
    frm = ('',) * n
    q = deque([(wp, frm, 1, 0, set())])
    opt = 0
    v = {}
    maxp = sum(r.values())

    while q:
        # worker pos, worker from, time, ttl pressure, opened valves
        wp, frm, t, ttl, opened = q.popleft()

        if v.get((t, wp), -1) >= ttl: 
            continue  # already know a better path to this state, so discard it
        v[t, wp] = ttl

        if t == ddt or len(opened) == len(r):
            # either all valves are open or time has run out
            opt = max(opt, ttl + maxp*(ddt-t))
            continue

        # compute choices for each worker
        choice = defaultdict(list) 
        for i, loc in enumerate(wp):
            if loc in r and loc not in opened:
                choice[i].append((loc, loc, set((loc,))))  # stay and open a valve
            for d in g[loc]:
                if d == frm[i] and loc not in opened: continue  # don't backtrack
                choice[i].append((d, loc, set()))  # move without opening a valve 

        # now that choices for each worker are described, queue all combinations
        # of those choices
        for cv in product(*choice.values()):
            newo = reduce(or_, (x[2] for x in cv), opened)
            nttl = ttl + sum(r[x] for x in newo)
            nwp = tuple(x[0] for x in cv)
            nfrm = tuple(x[1] for x in cv)
            q.append((nwp, nfrm, t+1, nttl, newo)) 
        
    return opt

print(run(g, r, 1, 30))
print(run(g, r, 2, 26))
