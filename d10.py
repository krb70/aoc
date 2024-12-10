import pathlib as P, sys as S, itertools as I
R, C = range, complex
_ = P.Path((S.argv+['d10.txt'])[1]).read_text().strip().split('\n')
G = {C(i,j):int(_[i][j]) for i,j in I.product(R(len(_)), R(len(_[0])))} 
paths, d = {}, {-1j**n for n in R(4)}

heads = set(k for k,v in G.items() if not v)

def search(p):
    if (v:=G[p]) == 9: paths[p] = {(p,)}
    for s in d:
        if G.get((nxt:=p+s), -1) != v+1: continue
        if nxt not in paths: search(nxt)
        subpaths = {(p,) + tail for tail in paths.get(nxt,set())}
        paths[p] = paths.get(p, set()) | subpaths

for h in heads: search(h)
# endpoints
print(sum(len(set(x[-1] for x in paths.get(h, {}))) for h in heads))
# paths
print(sum(len(paths.get(h, {})) for h in heads))
