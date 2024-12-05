from pathlib import Path
import itertools as itl

txt = Path('d2.txt').read_text().strip()
reports = [[int(x) for x in line.split()] for line in txt.split('\n')]

def issafe(lvls):
   diffs = [a-b for a,b in zip(lvls, itl.islice(lvls, 1, None))]
   if all(x<0 for x in diffs) or all(x>0 for x in diffs):
      if all(1 <= abs(x) <= 3 for x in diffs):
         return True

safe = list(filter(issafe, reports))

print(len(safe))

rm = lambda lvls, n: lvls[:n] + lvls[n+1:]

issafe2 = lambda lvls: any(issafe(x) for x in (rm(lvls, n)
                           for n in range(-1, len(lvls))))

safe = list(filter(issafe2, reports))

print(len(safe))
