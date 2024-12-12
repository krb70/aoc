import sys as S, pathlib as P, itertools as I, collections as C, operator as O, types
_=P.Path((S.argv+['d12.txt'])[1]).read_text().strip().split('\n')
X,Y,NS,R,PROD = len(_), len(_[0]),types.SimpleNamespace, range, I.product
PTS = set(I.starmap(complex,PROD(R(X),R(Y))))
G=C.defaultdict(str, {c:_[int(c.real)][int(c.imag)] for c in PTS})
N = {1j**n for n in R(4)}  # neighbors

def fill(v, pt, plot):
    if pt in plot.area|plot.per: return
    if G[pt]==v:
        plot.area.add(pt)
        for s in N: fill(v, pt+s, plot)
    else:
        plot.per.add(pt)
    return plot

def plots():
    res, seen = [], set()
    for pt in filter(lambda _: _ not in seen, PTS):
        seen |= (plot:=fill(G[pt], pt, NS(area=set(), per=set()))).area 
        res.append(plot)
    return res

def perim(p):
    return sum(1 for pt,n in PROD(p.per,N) if pt+n in p.area)

print(sum(len(p.area)*perim(p) for p in plots()))

def sides(p):
    def line(pt, nbr):
        'find span collinear with pt that has plot on nbr side'
        span = O.or_(*(set(I.takewhile(lambda pt:pt in p.per and pt+nbr in p.area,
                                       (pt-n*k*nbr*1j for k in R(max(X,Y)))))
                       for n in (1,-1)))
        return (frozenset(span), nbr)
    return len(set(line(pt,d) for pt,d in PROD(p.per,N) if pt+d in p.area))
    
print(sum(len(p.area)*sides(p) for p in plots()))

