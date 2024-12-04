
import sys
print((data:=sys.stdin.read()) and
      [next(iter((i+n for i in range(len(data))
                  if len(set(data[i:i+n]))==n)))
       for n in (4,14)])

# simulate a 1 byte at a time stream
def strm(data=data):
    for c in data: yield c

# Accumulate and yield delimited elements
# of the stream
def data_split(s,n):
    p = []
    for i,c in enumerate(s):
        p.append(c)
        if len(set(p[-n:])) == n:
            yield (i+1, ''.join(p[:-n]))
            p = []

import pprint
packets = list(data_split(strm(), 4))
data2 = ''.join(x[1] for x in packets[1:])
print(data2)
msgs = list(data_split(strm(data2), 14))
print(msgs)
#pprint.pprint(packets)
#pprint.pprint(msgs)
#print( packets[0][0] ) 
#print( msgs[0][0] ) 

