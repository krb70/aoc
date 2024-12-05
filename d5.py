import sys
from pathlib import Path
from functools import cmp_to_key as c2k

p = Path((sys.argv+['d5.txt'])[1]).read_text().strip().split('\n\n')
rtxt, ptxt = [x.split('\n') for x in p]
b4 = {tuple(int(x) for x in line.split('|')) for line in rtxt}
upd = [[int(x) for x in line.split(',')] for line in ptxt]

bad = lambda pn: any((b,a) in b4 for i, a in enumerate(pn) for b in pn[i+1:])

print(sum(pn[len(pn)//2] for pn in upd if not bad(pn)))

cmp = lambda a,b: -1 if (a, b) in b4 else (1 if (b,a) in b4 else 0)

print(sum(sorted(pn,key=c2k(cmp))[len(pn)//2] for pn in upd if bad(pn)))
