import sys as S, pathlib as P, itertools as I
_r, _p = P.Path((S.argv+['d17.txt'])[1]).read_text().strip().split('\n\n')
A,B,C = [int(x.split(':')[-1].strip()) for x in _r.split('\n')]
prog = [int(x) for x in _p.split(':')[-1].strip().split(',')]

def run(A,B,C,prog):
    co = lambda v: (v,v,v,v,A,B,C)[v]
    def adv(o): nonlocal A; A = A//2**co(o)
    def bxl(o): nonlocal B; B = B^o
    def bst(o): nonlocal B; B = co(o)%8
    def jnz(o): nonlocal cnt; cnt = o-2 if A else cnt
    def bxc(o): nonlocal B; B = B^C
    def out(o): vals.append(co(o)%8)
    def bdv(o): nonlocal B; B = A//2**co(o)
    def cdv(o): nonlocal C; C = A//2**co(o)
    cnt, vals, ops = 0, [], [adv,bxl,bst,jnz,bxc,out,bdv,cdv]
    while cnt<len(prog): 
        ops[prog[cnt]](prog[cnt+1])
        cnt += 2
    return vals

print(','.join(map(str,run(A,B,C,prog))))

def bestA(prog):
    t=0
    def v0(A):
        nonlocal t
        print(t:=t+1, oct(A)[2:])
        return run(A,0,0,prog)[0]  # run the program, return first value
    A_=lambda p,d='': int(p+str(d),8) # concat p and d as octals
    match=lambda p,d: (str(i) for i in range(8) if v0(A_(p,i))==d) # good digits to add
    first=lambda it: next(filter(None, it), 0)  # first truthy value of an iterable
    find=lambda pg,p='': first(find(pg[:-1],p+d) for d in match(p,pg[-1])) if pg else A_(p)
    return find(prog)
print(bestA(prog))
