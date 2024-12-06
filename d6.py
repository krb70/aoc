import pathlib as pl
import itertools as itl
import sys

grid = list(map(list, pl.Path((sys.argv+['d6.txt'])[1]).read_text().strip().split('\n')))

X, Y = len(grid), len(grid[0])
stepd = (-1, 1j, 1, -1j)

atpos = lambda p: grid[int(p.real)][int(p.imag)] if 0 <= p.real < X and 0 <= p.imag < Y else ' '
def put(p, c): grid[int(p.real)][int(p.imag)] = c

start = [p for a,b in itl.product(range(X), range(Y)) if atpos(p := complex(a,b)) == '^'][0]

def walk(pos, d):
    vs = set()
    loop = set()
    while True:
        if (pos, d) in loop:
            return vs, True
        vs.add(pos); loop.add((pos, d))
        match atpos(pos+stepd[d]):
            case ' ': break
            case '#': d = (d+1)%4 
            case _: pos = pos+stepd[d]
    return vs, False

print(len(walk(start, 0)[0]))

def walk2(pos, d, ad):
    old = atpos(ad)
    put(ad, '#')
    result = walk(pos, d)
    put(ad, old)
    print(ad, result[1])
    return result
    
print(sum(1 for a, b in itl.product(range(X), range(Y))
      if atpos(p:=complex(a,b)) == '.' and walk2(start, 0, p)[1]))

