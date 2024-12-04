import sys, pdb, numpy
from itertools import repeat
from collections import deque

inp = numpy.array([int(x.strip()) for x in open(sys.argv[1]).readlines()])

def mix(nbrs, fact=1, times=1):
    orig = list(enumerate(nbrs*fact))
    circ = deque(orig)
    for itm in repeat(orig, times):
        # put the i_th element in the correct relative position
        pos = circ.index(itm)
        circ.rotate(-pos)
        circ.popleft()
        circ.rotate(-itm[1])   
        circ.appendleft(itm)

    # find the zero position
    zoff = [i for i, x in enumerate(circ) if x[1] == 0][0]
    # compute the puzzle answer
    return sum(circ[(k + zoff) % len(nbrs)][1] for k in (1000, 2000, 3000))

print(mix(inp))
print(mix(inp, 811589153 , 10))
