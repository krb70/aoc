
import sys
import pandas as pd

df = pd.read_csv(sys.stdin, sep=' ', header=None, names=list('OM'))
M = [[0,1,2],
     [2,0,1],
     [1,2,0]]
df = df.apply(lambda c:c.apply(ord))
df = df - [min(df.O), min(df.M)]

def score(r):
    return 3*(((r.M-r.O)+1)%3) + r.M + 1

def score2(r):
    m = M[(r.O+2)%3][r.M]
    return 3*(((m-r.O)+1)%3) + m + 1

a1 = sum(score(r) for r in df.itertuples())
a2 = sum(score2(r) for r in df.itertuples())

print(a1, a2)
