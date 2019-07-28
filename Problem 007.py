# Problem 7 from Project Euler (projecteuler.net)

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

from math import *

# Decided to code up a prime list generator myself.
def primeNum(e):
    primes = [2]
    x = 3
    while len(primes) < e:  
        for p in primes:
            if p > sqrt(x):
                primes.append(x)
                break
            if x % p == 0: break
        else: primes.append(x)
        x += 2
    return primes[-1]

print(primeNum(10001))
