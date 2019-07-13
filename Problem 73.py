from pyprimes import *
from gmpy2 import *
from time import *

def otoh1(n):
    facs = [set(factors(n)) for n in xrange(n+1)]
    prime = [is_prime(n) for n in xrange(n+1)]

    def islowest(a,b):
        fa = facs[a]
        fb = facs[b]
        if fb-fa == fb: return True
        return False
    
    tot = 0
    for x in xrange(5,n+1):
        for y in xrange(x/3,x/2):
            if islowest(x,y): tot += 1
    return tot

def otoh2(n):
    fracs = set()
    for y in xrange(5,n+1):
        for x in xrange(y/3+1,y/2):
            fracs.add(1.0*x/y)
    return len(fracs)

def otoh3(n):
    j = {}
    for b in xrange(5,n+1):
       for a in xrange(b/3+1,b/2):
             j[1.0*a/b] = 1
    return len(j)

start = time()
print otoh1(12000)
print time()-start
start = time()
print otoh2(12000)
print time()-start
start = time()
print otoh3(12000)
print time()-start
