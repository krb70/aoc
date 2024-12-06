import sys as S, pathlib as P, itertools as I, collections as C

grid = list(map(list,P.Path((S.argv+['d6.txt'])[1]).read_text().strip().split('\n')))
R, X, Y, *stepd = range, len(grid), len(grid[0]), -1, 1j, 1, -1j
G = lambda: I.starmap(complex, I.product(R(X), R(Y)))
_atpos=lambda p:0<=(i:=int(p.real))<X and 0<=(j:=int(p.imag))<Y and grid[i][j] or ''
atpos = C.defaultdict(str, {p:_atpos(p) for p in G()})
nxt=lambda p,d: p+stepd[d]
put = atpos.__setitem__

start = next(filter(lambda p: atpos[p]=='^', G()))

def walk(pos, d):
    vs, loop = [pos], set()
    while True:
        if pos != vs[-1]: vs.append(pos)
        match atpos[n:=nxt(pos,d)]:
            case '': break
            case '#':
                d = (d+1)%4  # right turn
                # detect loops at each turn position
                if (pos,d) in loop: return
                loop.add((pos,d))
            case _: pos = n
    return vs

route = walk(start, 0)
print(len(set(route)))

def walk2(pos, d, ad):
    return (put(ad, '#'), walk(pos, d), put(ad, '.'))[1]

print(sum(1 for p in set(route)-{start} if atpos[p]=='.' and not walk2(start, 0, p)))

