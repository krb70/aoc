import sys as S, pathlib as P, functools as F, re
tw,pats = P.Path((S.argv+['d19.txt'])[1]).read_text().strip().split('\n\n')
tw,sw = re.findall(r'\w+',tw), str.startswith

find = F.cache(lambda p:sum(find(p[len(t):]) for t in tw if sw(p,t)) if p else 1)
print(len(sols:=list(filter(None,map(find,pats.split())))),sum(sols),sep='\n')
