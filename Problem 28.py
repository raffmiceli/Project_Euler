from math import *

def diagsum(x):
    s = 1
    for n in xrange(3,x+1,2):
        for m in xrange(4):
            s += n**2-m*(n-1)
    return s

#print diagsum(1001)

def diagSum(x):
    return 1+sum(n**2-m*(n-1) for n in xrange(3,x+1,2) for m in xrange(4))

#print diagSum(1001)

def DiagSum(x):
    return 1+sum(4*n**2-6*n+6 for n in xrange(3,x+1,2))

#print DiagSum(1001)

def DiagSumT(x):
    s,d,t = 1,2,3
    while t <= x**2:
        s += t
        t += d
        if not sqrt(t)%1: d += 2
    return s

print DiagSumT(1001)
