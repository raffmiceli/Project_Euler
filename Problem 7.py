from math import *

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

print primeNum(10001)
