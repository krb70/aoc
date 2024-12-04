import sys, re, pprint
from collections import defaultdict, deque

inp = open(sys.argv[1]).readlines()

bps = [{x: int(y) for x, y in m.groupdict().items()}
       for line in inp
       if (m := re.search(r"""(?x)
          print\s(?P<id>\d+).*?
                 (?P<ore>\d+).*?
                 (?P<orecly>\d+).*?
                 (?P<obsore>\d+).*?
                 (?P<obscly>\d+).*?
                 (?P<geoore>\d+).*?
                 (?P<geoobs>\d+).*?""", line))]

def sim(bp, N):
    rb = defaultdict(int)
    rb['ore'] = 1
    qty = defaultdict(int)
    cst = {'ore' : {'ore': bp['ore']},
           'cly' : {'ore': bp['orecly']},
           'obs': {'ore': bp['obsore'], 'cly': bp['obscly']},
           'geo': {'ore': bp['geoore'], 'obs': bp['geoobs']}}

    q = deque([(0, rb, qty)])
    best = 0 
    while q:
        t, rinv, oinv = q.popleft()
        if t == N:
            best = max(best, oinv['geo'])
            continue

        noinv = defaultdict(int)
        noinv.update(oinv)
        for prd, cnt in rinv.items():  # robots making products
            noinv[prd] += cnt
 
        for prd, need in cst.items():
            if all(oinv[x]>need[x] for x in need):  # can make this robot 
                nrinv = defaultdict(int)
                nrinv.update(rinv)
                aoinv = defaultdict(int)
                aoinv.update(noinv)
                for p, a in need.items():
                    aoinv[p] -= a
                nrinv[prd] += 1
                q.append((t+1, nrinv, aoinv)) 
        q.append((t+1, dict(rinv), noinv))
        print(f"time {t}, qs = {len(q)}")

    return best

for i, bp in enumerate(bps):
    print(i+1, sim(bp, 24))

