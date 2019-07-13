from math import *
from pyprimes import *

def isPrime(n):
    if n < 2: return False
    x = 2
    while x <= sqrt(n):
        if n%x == 0: return False
        x += 1
    return True

l1 = ['1','2','3','4','5','6','7']
big = 0
for a in l1:
    l2 = [a]
    for b in list(set(l1) - set(l2)):
        l2 = [a,b]
        for c in list(set(l1) - set(l2)):
            l2 = [a,b,c]
            for d in list(set(l1) - set(l2)):
                l2 = [a,b,c,d]
                for e in list(set(l1) - set(l2)):
                    l2 = [a,b,c,d,e]
                    for f in list(set(l1) - set(l2)):
                        l2 = [a,b,c,d,e,f]
                        for g in list(set(l1) - set(l2)):
                            n = int(a+b+c+d+e+f+g)
                            if isprime(n):
                                #print n
                                if n > big: big = n
print big

check = [str(n) for n in xrange(1,8)]
for n in xrange(7654321,1234567,-2):
    if sorted(str(n)) == check and isprime(n):
        print n; break

##check, n = [str(n) for n in xrange(1,8)], 7654321
##while True:
##    if sorted(str(n)) == check and isprime(n):
##        print n; break
##    n -= 2

##l1 = list(primes_below(7654321))
##l2 = list(primes_below(1234567))
##primes = sorted(list(set(l1)-set(l2)))[::-1]
##check = [str(n) for n in xrange(1,8)]
##for p in primes:
##    if sorted(str(p)) == check: print p; break
