# Problem 3 from Project Euler (projecteuler.net)

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from primeList import *
from pyprimes import *

# Solution using my own prime-finding function, defined in another file so it would be easy to use for other problems.
e = 600851475143
#e = 100
for n in list(primes_below(10000)):
    while e%n == 0:
        e = e/n
        print(n, e)
    if e == 1: break

# Lazy way using pyprimes
n = 600851475143
print(factors(n))

# This was another user's soluction that I liked. I think the forum post got deleted so I can't properly credit them...

##def large_prime_factor(n):                                                           
##    if n==0 or n==1:                                                                         
##        return n
##    #trick to find out if n is power of 2 with bitwise operator &                    
##    if n & (n - 1) == 0:                                                             
##        return 2                                                                     
##    x=3                                                                              
##    while n<>1:                                                                      
##        if n%x==0:                                                                   
##            n=int(n/x)                                                               
##        else:                                                                        
##            x+=2                                                                     
##    return x                                                                         
##                                                                                     
##print(large_prime_factor(600851475143))
