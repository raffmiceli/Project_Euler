from pyprimes import *
from gmpy2 import is_prime
from operator import *
from math import *
from time import *

def phi(n):
    if is_prime(n): return n-1
    res = n
    facs = set(factors(n))
    for p in facs:
        res *= p-1
        res /= p
    return res

def totperm(e):
    m,mp,n = 0,2,3
    while n < 10**e:
        p = phi(n)
        if sorted(str(n)) == sorted(str(p)):
            np = float(n)/p
            if np < mp:
                m,mp = n,np
                #print n,np
        n += 2
    print m, mp

#print totperm(7)

def totPerm(e):
    lim = 10**e
    sq = int(lim**.5)
    d = int(2*log(e))*1000
    primes = [p for p in list(primes_below(sq+d)) if p > sq-d]
    pairs = [(a,b) for a in primes for b in primes \
             if a*b < lim \
             and not (a+b-1)%9 \
             and a < sq and b > sq]
    m,mp = 0,2
    for pair in pairs:
        n = reduce(mul,pair)
        p = (pair[0]-1)*(pair[1]-1)
        if sorted(str(n)) == sorted(str(p)):
            np = float(n)/p
            if np < mp:
                m,mp = n,np
                #print n,np
    print m, mp

start = time()
totPerm(7)
print time()-start
