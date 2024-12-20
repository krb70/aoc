import sys as S, pathlib as P, itertools as I
C,R,d=complex,range,{1j**n for n in range(4)}
txt = P.Path((S.argv+['d20.txt'])[1]).read_text().strip().split('\n')
X,Y=len(txt[0]),len(txt)
G = {C(x,y):c for x,y in I.product(R(X),R(Y)) if (c:=txt[y][x]) in '.SE'}
N, p = len(G), next(p for p,v in G.items() if v=='S')

for i in R(len(G)):
    G[p],p=i,p+next((k for k in d if str(G.get(p+k,'#')) in '.E'),0)
iG = {v:k for k,v in G.items()}

md = lambda a: int(abs(a.real)) + int(abs(a.imag))

def cheats(sz=2, goal=100):
    nbrs = (c for x in I.product(R(-sz,sz+1),R(-sz, sz+1)) if md(c:=C(*x))<=sz)
    for p,n in I.product(R(N-goal), nbrs):
       if (_2:=(_1:=iG[p])+n) in G and G[_2]-G[_1]-md(n)>=goal: yield (_1,_2)

print(sum(1 for _ in cheats()))
print(sum(1 for _ in cheats(20)))
