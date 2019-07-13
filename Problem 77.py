from pyprimes import *

def psums(n):
    ps = list(primes_below(n))
    vals = [1]+[0]*n
    for i in xrange(len(ps)):
        for j in xrange(ps[i],n+1):
            vals[j] += vals[j-ps[i]]
    return vals[-1]

##for n in xrange(30):
##    print n, psums(n)

n = 3
while True:
    ps = psums(n)
    if ps > 5000:
        print n, ps
        break
    n += 1

##def fpsum(n):
##    ps = list(primes_below(5))
##    p = primes_above(5)
##    vals = [1]+[0]*ps[-1]
##    while True:
##        for i in xrange(len(ps)):
##            for j in xrange(ps[i],ps[-1]+1):
##                vals[j] += vals[j-ps[i]]
##        if vals[-1] > n: break
##        ps.append(next(p))
##        while len(vals) != ps[-1]+1:
##            vals.append(0)
##    return vals
