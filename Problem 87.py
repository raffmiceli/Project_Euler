from pyprimes import *

m = 5*10**7
l2 = int(m**(1./2)); p2 = list(primes_below(l2))
l3 = int(m**(1./3)); p3 = list(primes_below(l3))
l4 = int(m**(1./4)); p4 = list(primes_below(l4))
true = set()

for a in p2:
    for b in p3:
        for c in p4:
            s = a**2+b**3+c**4
            if s < m: true.add(s)
print len(true)
