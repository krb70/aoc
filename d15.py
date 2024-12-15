import sys as S, pathlib as P, itertools as I
R, C=range, complex
_map,moves = [x.strip() for x in P.Path((S.argv+['d15.txt'])[1]).read_text().split('\n\n')]
_map = _map.split('\n')
moves = moves.replace('\n','')

X, Y = len(_map), len(_map[0])
G={C(x,y):_map[x][y] for x,y in I.product(R(X), R(Y))}
rb = next((p for p, v in G.items() if v=='@'))
moves = [{'^':-1, '>':1j, 'v':1, '<':-1j}[c] for c in moves]

show = lambda G: print('\n'.join(ln for x in R(X) if (ln:=''.join(G[C(x,y)] for y in R(Y)))))

def push(G, p, d):  # push from the p position in d direction
    if (n:=p+d) not in G or G[n] == '#': return False
    if G[n] == '.' or push(G, n, d):
        G[n], G[p] = G[p], '.'
        return True

gps = lambda p: int(100*p.real + p.imag) 
for m in moves:
    if push(G, rb, m): rb += m
print(sum(gps(p) for p,c in G.items() if c=='O'))

_map = [''.join({'.':'..', 'O':'[]', '#': '##', '@': '@.'}[c] for c in ln) for ln in _map]
Y = len(_map[0])
G={C(x,y):_map[x][y] for x,y in I.product(R(X), R(Y))}
rb = next((p for p, v in G.items() if v=='@'))

def push2(G, p, d):
    if d.imag: return push(G, p, d)  # left/right no difference
    if G[p]=='@':
        if G[n:=p+d] == '#': return False  # wall, no move
        if G[n] == '.' or push2(G, n, d):
            G[p], G[n] = G[n], '@'
            return True
    if G[p]==']': p-=1j # find left side of box
    if '#' in (G[n:=p+d], G[n+1j]): return False
    G2 = G.copy()
    if (G2[p+d]=='.' or push2(G2,n,d)) and (G2[n+1j]=='.' or push2(G2,n+1j,d)):
        G.update(G2)  # all downstream boxes moved
        G[n], G[n+1j], G[p], G[p+1j] = G[p], G[p+1j], '.', '.'
        return True

for m in moves:
    if push2(G, rb, m): rb += m
print(sum(gps(p) for p,c in G.items() if c=='['))

