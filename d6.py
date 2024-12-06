import sys as S, pathlib as P, itertools as I, collections as C

grid = P.Path((S.argv+['d6.txt'])[1]).read_text().strip().split('\n')
R, X, Y = range, len(grid), len(grid[0])
G = lambda: I.starmap(complex, I.product(R(X), R(Y)))
loc = C.defaultdict(str, {p:grid[int(p.real)][int(p.imag)] for p in G()})
put = loc.__setitem__

start = next(filter(lambda p: loc[p]=='^', G()))

def walk(pos, d):
    vs, loop = [pos], C.Counter()
    while v:=loc[n:=pos+d]:
        if v == '#': # detect loops at each turn position
            d *= -1j  # right turn
            if loop.update({(pd:=(pos,d)):1}) or loop[pd]>1: return
        else: pos, _ = n, vs.append(n)
    return vs

rt = walk(start, -1)
print(len(set(rt)))

walk2 = lambda pos, d, ad: (put(ad, '#'), walk(pos, d), put(ad, '.'))[1]

cand = {p2:p1 for p1,p2 in reversed(list(I.pairwise(rt))) if p1!=p2}
print(sum(1 for p2, p1 in cand.items() if p2!=start and not walk2(p1, p2-p1, p2)))

