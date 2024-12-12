import sys as S, pathlib as P, functools as F
((T := list(map(int,P.Path((S.argv+['d11.txt'])[1]).read_text().strip().split()))), print([sum(N(s, k) for s in T if (N:=F.cache( lambda s,n: ((o:=n-1)<0 and 1) or (not s and N(1,o)) or ((k:=len(d:=str(s)))%2 and N(2024*s,o)) or N(int(d[:(m:=k//2)]),o)+N(int(d[m:]),o)))) for k in (25, 75)]))
