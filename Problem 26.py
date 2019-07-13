from eraSieve import *
from pyprimes import *

def reptends(n):
    #primes = eraSieve(n)
    primes = list(primes_below(x))
    reptends = []
    for p in primes:
        if 10**(p-1)%p == 1:
            for m in xrange(2,p/2+2):
                if 10**(p-m)%p == 1: break
            else: reptends.append(p)
    return reptends[-1]

#print reptends(1000)

def reptendl(n):
    #primes = eraSieve(n)[::-1]
    primes = list(primes_below(x))[::-1]
    for p in primes:
        if pow(10,p-1,p) == 1:
            for m in xrange(2,p/2+2):
                if pow(10,p-m,p) == 1: break
            else: return p

#print reptendl(1000)

def cycle(n):
    while not n%2: n /= 2
    while not n%5: n /= 5
    if n == 1: return 0
    for m in range(1,n):
        if pow(10,m,n) == 1:
            return m
    return None

def maxCycle(a):
    ma,mac = 0,0
    for n in range(2,a+1):
        c = cycle(n)
        if c > mac:
            ma,mac = n,c
    return (ma,mac)

print maxCycle(1000)
        
    
