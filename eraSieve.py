import math
def eraSieve(x):
    primes = [2] + range(3, x+1, 2)
    n = 3
    a = 1
    while n <= math.sqrt(x):
        for m in primes:
            if m%n == 0 and m > n:
                primes.remove(m)
        a += 1
        n = primes[a]
    return primes
