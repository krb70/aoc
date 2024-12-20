import sys as S, pathlib as P, itertools as I, collections as O
C,R,d=complex,range,{1j**n for n in range(4)}

txt = P.Path((S.argv+['d20.txt'])[1]).read_text().strip().split('\n')
G = {C(x,y):c for x,y in I.product(R(len(txt[0])),R(len(txt))) if (c:=txt[y][x]) in '.SE'}
S,E = [p for k in 'SE' for p,v in G.items() if v==k]
assert G[S] == 'S' and G[E] == 'E' and all(G[k]=='.' for k in G if k not in [S,E])
p=S

def show():
    for y in R(len(txt)):
       ln = ''.join(str(G.get(C(x,y),'#'))[-1] for x in R(len(txt[0])))
       print(ln)
    print()

for i in R(len(G)):
    G[p],p=i,p+next((k for k in d if str(G.get(p+k,'#')) in '.E'),0)

iG = {v:k for k,v in G.items()}

assert iG[0] == S and iG[len(G)-1] == E
def cheats():
    for i in R(len(G)):
        s1 = [p for k in d if (p:=iG[i]+k) not in G]
        for _1 in s1:
            s2 = [p for k in d if (p:=_1+k) in G and p!=iG[i]]
            for _2 in s2:
                score = G[_2]-G[iG[i]] - 2
                if score > 0:
                    yield ((_1, _2), score)

print(sum(1 for (_1, _2), s in cheats() if s>=100))

