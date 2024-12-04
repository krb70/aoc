import sys
from pathlib import Path
from itertools import product
L, S, R, F, N, P, C, I, T = len, sum, range, filter, None, product, complex, int, set

fn = (sys.argv + ['d4.txt'])[1]
lines = list(F(N, Path(fn).read_text().split('\n')))

X, Y = L(lines), L(lines[0])
word = 'XMAS'
rose = T(C(a, b) for a, b in P(R(-1, 2), R(-1, 2))) - {0}
char = lambda pos: lines[I(pos.real)][I(pos.imag)]

def search(pos, depth=0, incr=0):
    if not (0 <= pos.real < X and 0 <= pos.imag < Y): return 0
    if char(pos) != word[depth]: return 0 
    if depth+1 == L(word): return 1
    return search(pos+incr, depth+1, incr)

print(S(search(C(r, j),0,d) for r, j in P(R(X),R(Y)) for d in rose))

ms = T('MS')
diags = (-1-1j, 1+1j), (1-1j, -1+1j)

x_mas = lambda pos: I(char(pos)=='A' and all({char(pos+x) for x in c}==ms for c in diags))
print(S(x_mas(C(x, y)) for x, y in P(R(1, X-1), R(1, Y-1))))  

