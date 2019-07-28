# Problem 5 from Project Euler (projecteuler.net)

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# This one's actually pretty doable by hand. Just list all the positive integers less than 20, work out their prime factorizations,
# then multiply together the primes less than 20, each raised to the highest power found in the factorizations.
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

# Function to find the highest power necessary for an integer.
def numPowers(x,n):
    y = 1
    while x**(y+1) <= n:
        y += 1
    return y

# Multiplies primes raised to correct power.
def lrgstNumDiv(n):
    t = 1
    for x in list(primes_below(n)):
        t *= x**numPowers(x,n)
    return t

print(lrgstNumDiv(20))

# There's a nice pythonic one-liner way to do this using logarithms and reduce:
from math import floor, log
from operator import mul
from functools import reduce
from pyprimes import primes_below

print(reduce(mul,[p**floor(log(20,p)) for p in primes_below(20)]))

