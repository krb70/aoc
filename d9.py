import pathlib as P, sys as S
R, N = range, -1
ln = list(map(int,P.Path((S.argv+['d9.txt'])[1]).read_text().strip()))
# construct disk image and indexes of used and free space
dsk, fl, spc = [], [], []
for i,d in enumerate(ln):
    if i%2: spc.append((len(dsk), d)), dsk.extend([N]*d)
    else: fl.append((len(dsk), d)), dsk.extend([i//2]*d)

s, e, odsk = 0, (D:=len(dsk)), dsk[:]
while e > s:
    fpos = next((i for i in R(s,e) if dsk[i]<0), D)
    blk = next((i for i in reversed(R(fpos, e)) if dsk[i]>=0), N)
    if fpos>blk: break
    dsk[fpos], dsk[blk] = dsk[blk], N 
    s, e = fpos+1, blk

print(sum(i*b for i, b in enumerate(dsk) if b>0))

# start over, move whole files
fposs, dsk = list(R(len(spc))), odsk[:]
for fln in reversed(R(len(fl))):
    flndx, sz = fl[fln]
    if (fposi := next((i for i in R(len(fposs)) if spc[fposs[i]][1]>=sz), N)) >= 0:
       fpos, av = spc[fposs[fposi]]
       if flndx <= fpos: continue # never move a file forward
       spc[fposs[fposi]] = (fpos+sz, av-sz)
       if av == sz: del fposs[fposi]
       dsk[fpos:fpos+sz], dsk[flndx:flndx+sz] = [dsk[flndx]]*sz, [N]*sz

print(sum(i*b for i, b in enumerate(dsk) if b>0))

