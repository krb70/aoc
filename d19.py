import sys as S, pathlib as P, functools as F
tw,pats = P.Path((S.argv+['d19.txt'])[1]).read_text().strip().split('\n\n')
tw = [_.strip() for _ in tw.split(',')]
pats = [_.strip() for _ in pats.split('\n')]

@F.cache 
def search(pat):
    return not pat and 1 or sum(search(pat[len(t):]) for t in tw if pat.startswith(t))

sols = [s for pat in pats if (s:=search(pat))]
print(len(sols))
print(sum(sols))
