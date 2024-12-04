import sys, pprint, pdb, copy
from operator import add, sub, mul, floordiv as div

lines = [x.strip() for x in open(sys.argv[1]).readlines()]

opmap = {'+': add, '-': sub, '*': mul, '/': div}

def tree(lines):
    mk = {}
    for ln in lines:
        name, val = ln.split(":")
        val = val.strip()
        if val.isdigit():
            mk[name] = int(val)
        else:
            a, op, b = val.split()
            mk[name] = (a, op, b)
    return mk

def evl(mk, n, humn=None):
    if n == 'humn' and humn is not None:
        return humn
    val = mk[n]
    if isinstance(val, int): return val

    x, op, y = val
    x = evl(mk, x, humn)
    y = evl(mk, y, humn)
    val = opmap[op](x, y)
    mk[n] = val
    return val 

mk = tree(lines)
print(evl(mk, 'root'))


mk = tree(lines)
left, _, right = mk['root']
mk['root'] = (left, '-', right)

print(evl(copy.deepcopy(mk), 'root', 3305669217842))

def guess(k):
    lmk = copy.deepcopy(mk)
    return evl(lmk, 'root', k)

def search(x, dx):
    fx = guess(x)
    pdb.set_trace() 
    while abs(fx) > 3*dx:
       fpx = (guess(x+dx) - fx) / dx
       x = int(x - fx/fpx)
       fx = guess(x)
 
    return (x, fx)
   
print(search(1000, 10))
