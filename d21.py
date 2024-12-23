import sys as S, pathlib as P, itertools as I, functools as F
C,EN,R,T,PW=complex,enumerate,range,tuple,I.pairwise
codes = P.Path((S.argv+['d21.txt'])[1]).read_text().strip().split()
pads = ["789 456 123 _0A".split(), "_^A <v>".split()]
k2p = [{c:C(x,y) for x,r in EN(pad) for y,c in EN(r)} for pad in pads]
ok = lambda a,b,c:a.real+b.imag*1j!=c  # stays on keypad? i.e no '_'?
ri = lambda x:(int(x.real),int(x.imag))
maybe = lambda p,v: p and {v} or set()

@F.cache
def paths(k1, k2, kp):
    a,b,sp = [k2p[kp][t] for t in (k1,k2,'_')]
    ud,lr = [ab[c<0]*abs(c) for ab,c in zip(('^v','<>'),ri(a-b))]
    return maybe(ok(a,b,sp),lr+ud) | maybe(ok(b,a,sp),ud+lr)

@F.cache
def combos(keys, kp):
    return T(T(p+'A' for p in paths(k1,k2,kp)) for k1,k2 in PW('A'+keys))

@F.cache
def seq(robot, cd, kp=1):
    return robot and sum(min(seq(robot-1,p) for p in t) for t in combos(cd,kp)) or len(cd)

print(sum(seq(3,code,0)*int(code[:3]) for code in codes))
print(sum(seq(26,code,0)*int(code[:3]) for code in codes))

for f in (paths, combos, seq): print(f.cache_info())
