from pathlib import Path
from collections import Counter

txt = Path('d1.txt').read_text()
nums = [[int(x.strip()) for x in line.split()] for line in txt.split('\n') if line]

cols = list(zip(*nums))
first = sorted(cols[0])
second = sorted(cols[1])

dist = sum(abs(a-b) for a,b in zip(first, second))
print(dist)

c = Counter(second)
print(sum(x*c[x] for x in first))
