import sys as S, pathlib as P, re, types, functools as F, itertools as I
from collections import Counter
C, NS = complex, types.SimpleNamespace

lines = P.Path((S.argv+['d14.txt'])[1]).read_text().strip().split('\n')
_ = [list(map(int, re.findall(r'[0-9\-]+', ln))) for ln in lines]
rb = [NS(p=C(*x[:2]), v=C(*x[-2:])) for x in _]
X, Y = int(max(_.p.real for _ in rb)+1), int(max(_.p.imag for _ in rb)+1)

pos = lambda r, t: C((p:=r.p+t*r.v).real%X, p.imag%Y)
lrm = lambda v, m: 0 if v<m else (1 if v>m else None)
quad = lambda p: None if None in (x:=lrm(p.real,X//2),y:=lrm(p.imag,Y//2)) else x+2*y

cnt = Counter(q for r in rb if (q:=quad(pos(r,100))) is not None)
print(F.reduce(lambda a,b:a*b, cnt.values()))

middle = lambda ps: [p for p in ps if (X/4<=p.real<=3*X/4) if (Y/4<=p.imag<=3*Y/4)]

# find when most robots are in the middle of the space
for s in range(100, 10000):
    mid = middle((pos(r,s) for r in rb))
    if len(mid) > .7*len(rb):
        print(s)
        print('\n'.join(ln.rstrip() for y in range(Y) if (ln:=''.join('*' if C(x,y) in mid else ' ' for x in range(X)))
               if len(ln.replace(' ',''))>3))
