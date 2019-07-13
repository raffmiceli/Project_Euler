from math import *
from eraSieve import *
from pyprimes import *
from datetime import datetime

def isPrime(n):
    x = 2
    if n < 2: return False
    else:
        while x <= sqrt(n):
            if n%x == 0: return False
            x += 1
        return True

def quadprime():
    ma,mb,mp = 0,0,0
    #cprimes = set(eraSieve(2000))
    #primes = eraSieve(1000)
    cprimes = set(list(primes_below(2000)))
    primes = list(primes_below(1000))
    mprimes = [-n for n in primes]
    for a in mprimes:
    #for a in xrange(-1,-1000,-2):
        for b in primes:
            if a > b: continue
            if (a+b+1) not in cprimes: continue
            ps,n = 0,1
            while isPrime(n**2+a*n+b):
                ps,n = ps+1,n+1
            if ps > mp:
                ma,mb,mp = a,b,ps
    print ma, mb, mp, ma*mb

start = datetime.now()
quadprime()
print datetime.now()- start

def qpcf(n):
    L = int((sqrt(4*n-163)-1)/2)
    a = -(2*L+1)
    b = (L**2+L+41)
    return (a,b)#,a*b)

print qpcf(100000)

##ma = 0
##mb = 0
##mp = 0
##
##start = datetime.now()
##print start
##
##for a in range(-999, 1000, 2):
##    #for b in range(-999, 1000, 2):
##    #for b in eraSieve(1000):
##    for b in list(primes_below(1000)):
##        ps = 0
##        for n in range(1,1000):
##            p = n**2+a*n+b
##            if p > 0:
##                if isPrime(p):
##                    ps += 1
##                else: break
##        if ps > mp:
##            ma = a
##            mb = b
##            mp = ps
##            print ma, mb, mp, ma*mb
##
##end = datetime.now()
##print end
##print end - start
