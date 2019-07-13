from math import *
from eraSieve import *
from pyprimes import *
from gmpy2 import *

def isPrime(n):
    x = 2
    if n < 2: return False
    while x <= sqrt(n):
        if n%x == 0: return False
        x += 1
    return True

##primes = eraSieve(10000)

##for m in range(50):
##    t = 0
##    a = []
##    t1 = 0
##    b = 0
##    primes = eraSieve(10000)[m:]
##    for n in primes:
##        t += n
##        if t > 1000000: break
##        a.append(n)
##        if isPrime(t):
##            t1 = t
##            b = len(a)
##    if b > bigl:
##        big = t1
##        bigl = b
##print big, bigl

primes = list(primes_below(10000))

big = 0
bigl = 0

for m in xrange(10):
    t,t1,a,b = 0,0,0,0
    for n in primes[m:]:
        t += n
        if t > 1000000: break
        a += 1
        if is_prime(t):
            t1,b = t,a
    if b > bigl:
        big,bigl = t1,b
        #print big, bigl
print big, bigl
