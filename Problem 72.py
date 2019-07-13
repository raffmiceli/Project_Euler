from pyprimes import *

def fareylen(n):
    phis = range(n+1)
    for p in primes_below(n):
        for a in xrange(p,n+1,p):
            phis[a] *= p-1
            phis[a] /= p
    #print phis
    return sum(phis[2:])

print fareylen(1000000)

def Fareylen(n):
    phis = range(n+1)
    for p in xrange(2,n+1):
        if p == phis[p]:
            for a in xrange(p,n+1,p): phis[a] -= phis[a]/p
    return sum(phis[2:])

print fareylen(12000)

