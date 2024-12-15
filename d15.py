import sys as S, pathlib as P, itertools as I, collections as O
R, C, CM=range, complex, O.ChainMap
_map,moves = [x.strip() for x in P.Path((S.argv+['d15.txt'])[1]).read_text().split('\n\n')]
_map = _map.split('\n')
moves = moves.replace('\n','')

X,Y = len(_map), len(_map[0])
G = {C(x,y):_map[x][y] for x,y in I.product(R(X), R(Y))}
rb = next((p for p, v in G.items() if v=='@'))
moves = [{'^':-1, '>':1j, 'v':1, '<':-1j}[c] for c in moves]

def swap(G,d,*p):
    for _ in p: G[_+d], G[_] = G[_], G[_+d]

push = lambda G,p,d: 0 if G[n:=p+d]=='#' or (G[n]!='.' and not push(G,n,d)) else (swap(G,d,p) or 1) 
gps = lambda p: int(100*p.real + p.imag) 

for m in moves:
    if push(G,rb,m): rb += m
print(sum(gps(p) for p,c in G.items() if c=='O'))

# grow the floor map in X dimension, re-calc grid and robot position
_map = [''.join({'.':'..', 'O':'[]', '#': '##', '@': '@.'}[c] for c in ln) for ln in _map]
Y = len(_map[0])
G = {C(x,y):_map[x][y] for x,y in I.product(R(X),R(Y))}
rb = next((p for p,v in G.items() if v=='@'))

def push2(G,p,d):
    if d.imag: return push(G, p, d)  # left/right no difference
    if G[p]=='@':
        return 0 if G[n:=p+d]=='#' or (G[n]!='.' and not push2(G,n,d)) else (swap(G,d,p) or 1)
    if G[p]==']': p-=1j  # left side of box
    if '#' in (G[n:=p+d], G[n+1j]): return 0 
    if ((G2:=CM({},G))[p+d]=='.' or push2(G2,n,d)) and (G2[n+1j]=='.' or push2(G2,n+1j,d)):
        return G.update(G2.maps[0]) or swap(G,d,p,p+1j) or 1

for m in moves:
    if push2(G,rb,m): rb += m
print(sum(gps(p) for p,c in G.items() if c=='['))
