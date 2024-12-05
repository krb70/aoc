from pathlib import Path
from collections import Counter

txt = Path('d1.txt').read_text().strip()
nums = [[int(x) for x in line.split()] for line in txt.split('\n')]

cols = [sorted(x) for x in zip(*nums)]
dist = sum(abs(a-b) for a,b in zip(*cols))
print(dist)
c = Counter(cols[1])
print(sum(x*c[x] for x in cols[0]))
