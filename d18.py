import sys as S, pathlib as P, collections as O
C=complex
txt = P.Path((S.argv+['d18.txt'])[1]).read_text().strip().split('\n')
S,N=71,1024
if len(txt)<100:
    S,N=7,12
bts = [C(*map(int,ln.split(','))) for ln in txt]

def search(n):
    q=O.deque([(C(0),)])
    G, good, seen=set(bts[:n]), [], set()
    while q:
        rt = q.popleft()
        if (pos:=rt[-1]) == C(S-1,S-1):
            good.append(rt)
            continue
        for i in range(4):
            p = pos+(-1j)**i
            if p in seen or p in G: continue
            if 0<=p.real<S and 0<=p.imag<S:
                seen.add(p)
                q.append(rt+(p,))
    best = good and min(len(rt) for rt in good)
    bestrt = next((rt for rt in good if len(rt) == best),())
    return bestrt

print(len(rt:=set(search(N)))-1)
for i, bt in enumerate(bts[N:]):
   if bt not in rt: continue
   if not (rt:=set(search(N+i+1))):
      print(f"{int(bt.real)},{int(bt.imag)}")
      break
