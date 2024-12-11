import sys as S, pathlib as P, functools as F
T = list(map(int,P.Path((S.argv+['d11.txt'])[1]).read_text().strip().split()))

@F.cache
def stonecnt(s, n):
    if not n: return 1
    if not s: return stonecnt(1, n-1)
    if (k:=len(d:=str(s)))%2: return stonecnt(2024*s, n-1)
    return stonecnt(int(d[:k//2]),n-1) + stonecnt(int(d[k//2:]),n-1) 

print(sum(stonecnt(s, 25) for s in T))
print(sum(stonecnt(s, 75) for s in T))

