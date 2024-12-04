import sys
from collections import deque
from operator import sub, add, setitem as si, getitem as gi

inp = [(dn[0], int(dn[1])) for line in sys.stdin.readlines() if (dn:=line.split())]

def flw(h,t):
    d = tuple(map(sub,h,t))
    return t if max(map(abs,d)) <= 1 else tuple(map(add,t,(r//abs(r) if r else r for r in d)))

def mv(h,d):
    f = {'U':(1,1), 'R':(0,1), 'L':(0,-1), 'D':(1,-1)}[d]
    return tuple(((r:=list(h)),si(r,f[0],gi(h,f[0])+f[1]))[0])

def pth(h,d,n):
    return (h:=mv(h,d) for _ in range(n)) 

pvz = lambda v: print('\n'.join(reversed([''.join(l) for l in v])))
def draw(h,s,ts):
    import time
    bs = [f(x) for x in ([y[i] for y in [h,s]+ts] for i in (0,1))
              for f in (min,max)]
    patch = [['.' for _ in range(bs[1]-bs[0] + 4)] for _ in range(bs[3]-bs[2]+4)]
    tr = lambda p: (p[0]-bs[0]+2, p[1]-bs[1]+2)  
    def put(p, c):
        p = tr(p)
        patch[p[1]][p[0]] = c
    for i,t in reversed(list(enumerate(ts,1))):
        put(t, str(i) if len(ts) > 1 else 'T')
    put(s, 's')
    put(h, 'H')
    pvz(patch)
    time.sleep(0.001)
    print('\n'*100)

ks, vd = [s:=(h:=(0,0))]*((N:=9)+1), {i: set([s]) for i in range(1,N+1)}
deque((deque(((si(ks,0,h),(p:=flw(ks[i],ks[i+1]))) and (si(ks,i+1,p) or gi(vd,i+1).add(p)) for i in range(N)),1) for m in inp for h in pth(ks[0],*m)), 1)

print({i: len(k) for i, k in vd.items() if i in (1,N)})

