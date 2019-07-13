from pyprimes import *
from gmpy2 import *
from time import *

primes = list(primes_below(10000))

def tlist(given,c):
    tgiven = sorted(set(given)-set(primes_below(c+1)))
    return sorted([p for p in tgiven if \
    isprime(int(str(c)+str(p))) and \
    isprime(int(str(p)+str(c)))])

def pps(ps):
    for a in ps:
        l1 = tlist(ps,a)
        for b in l1:
            l2 = tlist(l1,b)
            for c in l2:
                l3 = tlist(l2,c)
                for d in l3:
                    l4 = tlist(l3,d)
                    for e in l4:
                        sol = [a,b,c,d,e]
                        print sol, sum(sol)
                        return
start = time()
pps(primes)
print time()-start

##def tlist(given,c):
##    tgiven = sorted(set(given)-set(primes_below(c)))
##    res = []
##    for p in tgiven:
##        if p == c: continue
##        c1 = int(str(c)+str(p))
##        c2 = int(str(p)+str(c))
##        if isprime(c1) and isprime(c2):
##            res.append(p)
##    return res
