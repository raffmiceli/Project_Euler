from pyprimes import *
from gmpy2 import *

def findm(n):
    ma,mc = 0,''
    for c in str(n):
        co = str(n).count(c)
        if co > ma:
            ma,mc = co,c
    return mc

l1 = list(primes_below(1000000))
l2 = list(primes_below(100000))
primes = sorted(list(set(l1)-set(l2)))
    
for p in primes:
    ch = findm(p)
    if str(p).count(ch) == 3 and ch != str(p)[-1]:
        can = [int(str(p).replace(ch,str(a))) for a in xrange(10)]
        nump = [c for c in can if is_prime(c)]
        if nump[0] == p and len(nump) == 8:
            print p, nump
            #break

##for p in primes:
##    dnums = [str(p).count(a) for a in list(set(str(p)))]
##    if 3 in dnums:
##        ch = str(p)[dnums.index(3)]
##        can = [int(str(p).replace(ch,str(a))) for a in xrange(10)]
##        nump = [c for c in can if is_prime(c)]
##        if nump[0] == p and len(nump) == 8:
##            print p, nump
##            break
