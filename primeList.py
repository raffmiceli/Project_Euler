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
