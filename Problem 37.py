from math import *
from pyprimes import *
from datetime import datetime

def isPrime(n):
    x = 2
    if n < 2: return False
    else:
        while x <= sqrt(n):
            if n%x == 0: return False
            x += 1
        return True

true = []
n = 20
start = datetime.now()
while len(true) < 11:
    if isPrime(n):
        sn = str(n)
        l = len(sn)
        for m in range(l):
            if not isprime(int(sn[m:])) or not isprime(int(sn[:l-m])): break
        else:
            true.append(n)
            print n
    n += 1
print true, sum(true)
print datetime.now()-start

start = datetime.now()
ps = list(primes_below(1000000))
true = []
for n in ps:
    if n > 20:
        sn = str(n)
        l = len(sn)
        for m in range(l):
            if not isprime(int(sn[m:])) or not isprime(int(sn[:l-m])): break
        else:
            true.append(n)
            print n
print true, sum(true)
print datetime.now()-start
        
