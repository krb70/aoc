import re, sys as S, os, pathlib as P, itertools as I
C = complex
lines = P.Path((S.argv+['d13.txt'])[1]).read_text().strip().split('\n')

vals = [[int(d) for d in re.findall(r'\d+',ln)] for ln in filter(None, lines)]
machines = [[C(*_) for _ in vals[i:i+3]] for i in range(0,len(vals),3)]

# cross multiply and subtract using complex arithmetic
cms = lambda a,b: (b*a.conjugate()).imag

def solve(a, b, p): # solve simultaneous eqns, check for non-neg int soln
    (x, r1), (y, r2) = divmod(cms(p,b),d:=cms(a,b)), divmod(cms(a,p), d)
    return not any((r1, r2)) and all((x>=0, y>=0)) and C(x, y) 

token = lambda s: int(3*s.real+s.imag)
print(sum(token(s) for x in machines if (s:=solve(*x))))

e = 1e13
print(sum(token(s) for a,b,p in machines if (s:=solve(a,b,p+C(e,e)))))
