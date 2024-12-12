import sys as S, pathlib as P, itertools as I, collections as C
from functools import reduce
G=P.Path((S.argv+['d12.txt'])[1]).read_text().strip().split('\n')
X,Y,PROD = len(G), len(G[0]), I.product
N = {1j**n for n in range(4)}  # neighbors

flatten = I.chain.from_iterable
def partition(pts):
    def step(sets, c):
        ms = {s for d in N for s in filter(lambda v: c+d in v, sets)}
        sets -= ms
        sets.add(frozenset({c} | set(flatten(ms))))
        return sets
    return reduce(step, pts, set())

byL = C.defaultdict(set) 
for x,y in PROD(range(X), range(Y)): byL[G[x][y]].add(complex(x,y))
areas = {a for l in byL.values() for a in partition(l)}

perim = lambda area: [frozenset(p for a in area if (p:=a+d) not in area) for d in N]

sides = lambda area: [s for perim in perim(area) for s in partition(perim)]

print(sum(len(area)*sum(len(x) for x in perim(area)) for area in areas))
print(sum(len(area)*len(sides(area)) for area in areas))

