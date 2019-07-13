##1 = 1
##2 = 2
##3 = 3
##4 = 2**2
##5 = 5
##6 = 2*3
##7 = 7
##8 = 2**3
##9 = 3**2
##10 = 2*5
##11 = 11
##12 = 2**2*3
##13 = 13
##14 = 2*7
##15 = 3*5
##16 = 2**4
##17 = 17
##18 = 2*3**2
##19 = 19
##20 = 2**2*5
##
##2**4*3**2*5*7*11*13*17*19

from primeList import *
from pyprimes import *

def numPowers(x,n):
    y = 1
    while x**(y+1) <= n:
        y += 1
    return y

def lrgstNumDiv(n):
    t = 1
    for x in list(primes_below(n)):
        t *= x**numPowers(x,n)
    return t

print lrgstNumDiv(20)
