import sys as S, pathlib as P, itertools as I, collections as O
C,R,d=complex,range,{1j**n for n in range(4)}
txt = P.Path((S.argv+['d20.txt'])[1]).read_text().strip().split('\n')
X,Y=len(txt[0]),len(txt)
G = {C(x,y):c for x,y in I.product(R(X),R(Y)) if (c:=txt[y][x]) in '.SE'}
N, p = len(G), next(p for p,v in G.items() if v=='S')

for i in R(len(G)):
    G[p],p=i,p+next((k for k in d if str(G.get(p+k,'#')) in '.E'),0)
iG = {v:k for k,v in G.items()}

md = lambda a,b: int(abs(a.real-b.real)) + int(abs(a.imag-b.imag))

def ncheats(steps=2, goal=100):
    cp = set()
    nbrs = set(filter(lambda x:md(C(*x),0j)<=steps, I.product(R(-steps,steps+1),R(-steps, steps+1))))
    for p,(dx, dy) in I.product(R(N-goal), nbrs):
       if (_2:=(_1:=iG[p])+C(dx,dy)) in G:
           if G[_2]-G[_1]-abs(dx)-abs(dy) >= goal: cp.add((_1,_2))
    return len(cp) 

print(ncheats(2))
print(ncheats(20))
