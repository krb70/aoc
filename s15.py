import re, sys

row = int(sys.argv[1])
inp = sys.stdin.readlines()
pairs = [list(map(int,m.groups())) for ln in inp if
         (m := re.search(r'x=(.*?), y=(.*?):.*x=(.*?), y=(.*)\s*$', ln))]

sn = [tuple(x[:2]) for x in pairs]
bn = [tuple(x[2:]) for x in pairs]
bns = set(bn)

xb = (min(x[0] for x in sn+bn), max(x[0] for x in sn+bn))
yb = (min(x[1] for x in sn+bn), max(x[1] for x in sn+bn))


def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

sbdists = [dist(a,b) for a,b in zip(sn, bn)]
vxs = (xb[0] - max(sbdists) - 1, xb[1] + max(sbdists) + 1)

def viz(pt):
    if pt in bns: return False
    for i in range(len(sn)):
        if dist(pt, sn[i]) <= sbdists[i]:
            return True 
    return False

print(xb)
print(yb)
print(sum(viz((i, row)) for i in range(vxs[0], vxs[1]+1))) 

maxsa = int(sys.argv[2])

