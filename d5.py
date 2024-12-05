import sys, pathlib as plb
from functools import cmp_to_key as K
from itertools import combinations as C

p = plb.Path((sys.argv+['d5.txt'])[1]).read_text().strip().split('\n\n')
rtxt, ptxt = [x.split('\n') for x in p]
b4 = {tuple(int(x) for x in line.split('|')) for line in rtxt}
upd = [[int(x) for x in line.split(',')] for line in ptxt]

bad = lambda pn: any((b,a) in b4 for a,b in C(pn, 2))

print(sum(pn[len(pn)//2] for pn in upd if 1-bad(pn)))

cmp = lambda a,b: -int((a,b) in b4) or int((b,a) in b4) or 0

print(sum(sorted(pn,key=K(cmp))[len(pn)//2] for pn in upd if bad(pn)))
