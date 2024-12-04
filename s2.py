
import pathlib
import pandas as pd
import io

d = pathlib.Path('./2.txt').read_text().strip().replace(' ', ',')

df = pd.read_csv(io.StringIO(d), header=None)
df.columns = list('AB')

print(df.head())
def outcome(r):
    if r in [('A', 'X'), ('B', 'Y'), ('C', 'Z')]: return 3
    if r in [('A', 'Z'), ('B', 'X'), ('C', 'Y')]: return 0
    return 6 

def sel(r):
    return {'X': 1, 'Y': 2, 'Z':3}[r[1]]


print(sum(outcome(r)  + sel(r) for r in df.itertuples(index=False)))

def outcome(r):
    return {'X': 0, 'Y':3, 'Z':6}[r[1]]

def sel(r):
    return {('A', 'X'): 3,
            ('A', 'Y'): 1,
            ('A', 'Z'): 2,
            ('B', 'X'): 1,
            ('B', 'Y'): 2,
            ('B', 'Z'): 3,
            ('C', 'X'): 2,
            ('C', 'Y'): 3,
            ('C', 'Z'): 1}[r]
print(sum(outcome(r)  + sel(r) for r in df.itertuples(index=False)))

