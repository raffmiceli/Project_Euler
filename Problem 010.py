# Problem 10 from Project Euler (projecteuler.net)

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# Same prime list generator from earlier problem(s), just added an accumulator in each step.
def primeSum1(e):
    primes = [2]
    x = 3
    t = 2
    while x <= e:  
        for p in primes:
            if x % p == 0: break
        else:
            primes.append(x)
            t += x
            #print(x, t)
        x += 2
    return t

#142913828922

from eraSieve import *
from pyprimes import *

# Used my own Sieve of Eratosthenes but then switched to the primes_below() function from the PyPrimes library.
def primeSum2(x):
    t = 0
    #primes = eraSieve(x)
    primes = list(primes_below(x))
    print('List of primes complete.')
    for prime in primes:
        t += prime
        #print prime, t
    return t

# Same as before but switched from summing through a for loop to just using the sum() method
def primeSum3(x):
    #primes = eraSieve(x)
    primes = list(primes_below(x))
    print('List of primes complete.')
    print(sum(primes))

# Implemented my own sieve of Eratosthenes with summation each time a prime is found. Pretty inefficient since
# it doesn't jump to the next prime, just increments by 2.
def primeSum4(n):
    marked = [0] * n
    value = 3
    s = 2
    while value < n:
        if marked[value] == 0:
            s += value
            i = value
            while i < n:
                marked[i] = 1
                i += value
        value += 2
    return s

# Not sure what I was doing with this one. Just seems like a copy of my first method but I replaced the step-by-step summation with
# a sum() function at the end.
def primeSum5(e):
    primes = [2]
    x = 3
    t = 2
    while x <= e:  
        for p in primes:
            if p > sqrt(x):
                primes.append(x)
                #t += x
                break
            if x % p == 0: break
        else:
            primes.append(x)
            #t += x
            #print(x, t)
        x += 2
    #return t
    return sum(primes)

print(primeSum5(2000000))

# Just a more condensed sieve implementation.
def sieve_prime(n):                                                                  
    index=list(range(n))                                                             
    for i in range(2,int(n**0.5)+1):                                                 
        if index[i]:                                                                 
            for m in range(i**2,n,i):                                                
                index[m]=0                                                           
    return [p for p in index if p][1:]                                               
                                                                                     
#print(sum(sieve_prime(2000000)))
