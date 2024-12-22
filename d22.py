import sys as S, pathlib as P, collections as O 
vals=list(map(int,P.Path((S.argv+['d22.txt'])[1]).read_text().strip().split()))
U,R,EN,D=16777216,range,enumerate,O.deque

rn = lambda x: (((x:=(((x:=((x<<6)^x)%U)>>5)^x)%U)<<11)^x)%U
rnk = lambda x,k: D((x:=rn(x) for _ in R(k)), 1)[0]

print(sum(rnk(v,2000) for v in vals))

s2b = O.defaultdict(dict)
for n,v in EN(vals):
    d,x,p = D((),4),v,v
    for i in R(2000):
        ch,p=((x:=rn(p))%10)-(p%10),x
        d.append(ch)
        if len(d)==4: s2b[tuple(d)].setdefault(n, x%10)

print(max(sum(v.values()) for v in s2b.values()))
