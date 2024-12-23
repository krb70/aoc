import sys as S, pathlib as P, collections as O
T=tuple
pairs=set(T(x.split('-')) for x in P.Path((S.argv+['d23.txt'])[1]).read_text().strip().split())

n2b=O.defaultdict(set)
for a,b in pairs: n2b[a].add(b), n2b[b].add(a)

tp=set()
for a,b in pairs:
    for c in (n2b[a] & n2b[b]):
        tp.add(T(sorted([a,b,c])))

print(sum(1 for t in tp if any(x.startswith('t') for x in t)))

def find(p,r=(),x=None):  # Bron-Kerbosch
    r,x = x is None and (set(),set()) or (r,x)
    if not (p or x): return {T(r)}
    res,u = set(),next(iter(p|x))
    for n in p-n2b[u]:
        res|=find(p&n2b[n],r|{n},x&n2b[n])
        p,x = p-{n},x|{n}
    return res 

m = ((len(r),r) for r in find(set(n2b)))
print(','.join(sorted(max(m)[1])))
