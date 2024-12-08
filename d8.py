import pathlib as P, sys as S, math
from itertools import combinations as combos

grid = P.Path((S.argv+['d8.txt'])[1]).read_text().strip().split('\n')
X, Y = len(grid), len(grid[0])
ant = {complex(a,b): grid[a][b] for a in range(X) for b in range(Y) if grid[a][b] != '.'}
freqs = set(ant.values())

ingrid = lambda p: (0 <= p.real < X) and (0 <= p.imag < Y)
anode = lambda p1, p2: 2*p1 - p2
nodes = lambda p1, p2: [n for x,y in ((p1,p2),(p2,p1)) if ingrid(n:=anode(x,y))]

allnodes = lambda freq, nf: set(n for p1, p2 in combos((p for p,v in ant.items() if v==freq), 2)
                                  for n in nf(p1, p2))

print(len(set(x for f in freqs for x in allnodes(f, nodes)))) 

nodes2 = lambda p1, p2: ((diff:=p2-p1), (d:=diff/math.gcd(int(diff.real), int(diff.imag))),
                         set(n for k in range(-X-Y, X+Y) if ingrid(n:=p1+k*d)))[-1]

print(len(set(x for f in freqs for x in allnodes(f, nodes2)))) 

