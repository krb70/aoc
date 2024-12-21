import sys as S, pathlib as P, itertools as I, functools as F
C,EN,R,T=complex,enumerate,range,tuple
codes = P.Path((S.argv+['d21.txt'])[1]).read_text().strip().split()
pads = ["789 456 123 _0A".split(), "_^A <v>".split()]
k2p = [{c:C(x,y) for x,r in EN(pad) for y,c in EN(r)} for pad in pads]
off=lambda a,b,c:a.real+b.imag==c  # might it go off the keypad? i.e hit '_'?
ri=lambda x:(int(x.real),int(x.imag))

@F.cache
def paths(k1, k2, kp):
    a,b,sp = [k2p[kp][t] for t in (k1,k2,'_')]
    ud,lr = [ab[c<0]*abs(c) for ab,c in zip(('^v','<>'),ri(a-b))]
    return off(b,a,sp) and {lr+ud} or (off(a,b,sp) and {ud+lr} or {lr+ud,ud+lr})

@F.cache
def combos(keys, kp):
    return T(T(p+'A'  for p in paths(k1,k2,kp)) for k1,k2 in I.pairwise('A'+keys))

@F.cache
def seq(robot, keys, kp=1):
    return sum(min(seq(robot-1,p) for p in t) for t in combos(keys,kp)) if robot else len(keys)

print(sum(seq(3,code,0)*int(code[:3]) for code in codes))
print(sum(seq(26,code,0)*int(code[:3]) for code in codes))
for f in (paths, combos, seq):
    print(f.cache_info())
