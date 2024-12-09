import pathlib as P, sys as S
R = range
ln = list(map(int,P.Path((S.argv+['d9.txt'])[1]).read_text().strip()))
# construct disk image and indexes of free and used space
dsk, fl, spc = [], [], []
for i,d in enumerate(ln):
    if i%2: spc.append((len(dsk), d)), dsk.extend([-1]*d)
    else: fl.append((len(dsk), d)), dsk.extend([i//2]*d)

s, odsk = 0, dsk[:]
for e in range(len(dsk)-1, -1, -1):
    fpos = next(i for i in R(s,e) if dsk[i]<0)
    blk = next((i for i in R(e,fpos,-1) if dsk[i]>=0), -1)
    if fpos>blk: break
    dsk[fpos], dsk[blk] = dsk[blk], -1
    s = fpos+1

print(sum(i*b for i, b in enumerate(dsk) if b>=0))

# start over, move whole files
fposs, dsk = list(R(len(spc))), odsk[:]
for fln in R(len(fl)-1, -1, -1):
    flndx, sz = fl[fln]
    if (fposi := next((i for i in R(len(fposs)) if spc[fposs[i]][1]>=sz), -1)) >= 0:
       fpos, av = spc[fposs[fposi]]
       if flndx <= fpos: continue # never move a file forward
       spc[fposs[fposi]] = (fpos+sz, av-sz)
       if av == sz: del fposs[fposi]
       dsk[fpos:fpos+sz], dsk[flndx:flndx+sz] = [dsk[flndx]]*sz, [-1]*sz

print(sum(i*b for i, b in enumerate(dsk) if b>=0))

