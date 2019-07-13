from math import *
from eraSieve import *
from pyprimes import *

##primes = eraSieve(10000)
##
##def primefacs(n):
##    facs = []
##    for m in primes:
##        if m > n/2: break
##        if n%m == 0:
##            facs.append(m)
##    return facs
##
##n = 100000
##while True:
##    #print len(primefacs(n)),
##    if len(primefacs(n)) == 4:
##        if len(primefacs(n+1)) == 4:
##            if len(primefacs(n+2)) == 4:
##                if len(primefacs(n+3)) == 4:
##                    break
##    n += 1
##print n

def facs4(n):
    return len(set(factors(n))) == 4

n = 100000
while True:
    if facs4(n):
        if facs4(n+1):
            if facs4(n+2):
                if facs4(n+3):
                    print n; break
    n += 1

##n = 100000
##while True:
##    if all([facs4(n+a) for a in range(4)]):
##        print n; break
##    n += 1
##
##a = b = c = d = 0
##n = 100000
##while True:
##    a = b
##    b = c
##    c = d
##    d = len(set(factors(n)))
##    if a == b == c == d == 4:
##        print n-3
##        break
##    n += 1
