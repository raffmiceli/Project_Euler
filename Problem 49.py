from math import *
from eraSieve import *
from pyprimes import *

##l1 = eraSieve(10000)
##l2 = eraSieve(1000)
##primes = sorted(list(set(l1)-set(l2)))

##for a in primes:
##    for b in primes:
##        if sorted(str(a)) == sorted(str(b)):
##            for c in primes:
##                if a != b and b != c and a != c:
##                    if sorted(str(a)) == sorted(str(b)) and sorted(str(b)) == sorted(str(c)):
##                        if abs(a-b) == abs(b-c):
##                            print a, b, c

l1 = list(primes_below(10000))
l2 = list(primes_below(1000))
primes = sorted(list(set(l1)-set(l2)))

for a in primes:
    sa = sorted(str(a))
    for b in primes[primes.index(a)+1:]:
        sb = sorted(str(b))
        if sa == sb:
            for c in primes[primes.index(b)+1:]:
                sc = sorted(str(c))
                if sa == sb == sc:
                    if b-a == c-b:
                        print str(a)+str(b)+str(c)
