def primeList(e):
    """
    Returns list of primes <= given number.
    """
    primes = []
    x = 2
    while x <= e:  
        for p in primes:
            if x % p == 0: break
        else: primes.append(x)
        x += 1
    return primes

# This could be improved by breaking out of the inner for loop when p exceeds sqrt(x), like so:
def primeList2(e):
    primes = [2]
    x = 3
    while x <= e:
        for p in primes:
            if not x % p: break
            if p > x**.5:
                primes.append(p)
                break
        x += 1
    return primes
