from math import *
from eraSieve import *
from pyprimes import *

##def isPrime(n):
##    x = 2
##    if n < 2: return False
##    while x <= sqrt(n):
##        if n%x == 0: return False
##        x += 1
##    return True
##
##for n in range(2,10001):
##    if not isPrime(n) and n%2 == 1:
##        for m in eraSieve(n):
##            a = sqrt((n-m)/2)
##            if a.is_integer(): break
##        else:
##            print n
##            break

primes = [2]
for n in range(3,10001,2):
    if isprime(n):
        primes.append(n)
        continue
    for p in primes:
        a = sqrt((n-p)/2)
        if not a%1: break
    else:
        print n       
