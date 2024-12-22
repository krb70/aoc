import sys as S, pathlib as P, collections as O, itertools as I
vals=list(map(int,P.Path((S.argv+['d22.txt'])[1]).read_text().strip().split()))
N,U,D,PW,T,SD=2000,2**24-1,O.deque,I.pairwise,tuple,dict.setdefault

rn = lambda x: (((x:=(((x:=((x<<6)^x)&U)>>5)^x)&U)<<11)^x)&U
rnk = lambda x,k: I.chain((x,),(x:=rn(x) for _ in range(k)))
print(sum(D(rnk(v,N),1)[0] for v in vals))

s2b = O.defaultdict(dict)
for n,v in enumerate(vals):
    d = D((),4)
    D((SD(s2b[T(d)],n,b) for p,x in PW(rnk(v,N)) if d.append((b:=x%10)-p%10) or len(d)==4),1)

print(max(sum(v.values()) for v in s2b.values()))
