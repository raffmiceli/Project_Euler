from pyprimes import *
from gmpy2 import *

def phi(n):
    if is_prime(n): return n-1
    res = n
    for p in set(factors(n)):
        res *= p-1
        res /= p
    return res

mphi,mn,n = 0,0,2
while n <= 1000000:
    nphi = float(n)/phi(n)
    if nphi > mphi:
        m,mphi = n,nphi
        print n,nphi
    n += 2
print m

n = 1
for p in primes():
    if n*p > 1000000: break
    n *= p
print n


lst = [1]*1000001
primes = primes_below(1000)

for p in primes:
    r = p/(p-1.)
    lst[p::p] = [r * c for c in lst[p::p]]

m = max(lst)
print m, lst.index(m)


    

    
