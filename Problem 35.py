from math import *
from pyprimes import *

def isPrime(n):
    x = 2
    if n < 2: return False
    else:
        while x <= sqrt(n):
            if n%x == 0: return False
            x += 1
        return True

s = [2]
ps = list(primes_below(1000000))
for p in ps:
    if any([not int(l)%2 for l in str(p)]): continue
    if p in s: continue
    temp = set([p])
    sp = str(p)
    l = len(sp)
    for m in range(l-1):
        sp = sp[-1]+sp[:-1]
        temp.add(int(sp))
        if int(sp) not in ps: break
    else: s = s+list(temp)
print sorted(s), len(s)

##s = [2,3,5,7]
##for n in range(11,1000000,2):
##    if any([not int(l)%2 for l in str(n)]): continue
##    if is_prime(n):
##        sn = str(n)
##        l = len(sn)
##        for m in range(l-1):
##            sn = sn[-1]+sn[:-1]
##            if not is_prime(int(sn)): break
##        else: s.append(n)
##print s, len(s)

##t = 0
##for n in range(1,1000000):
##    if isPrime(n):
##        sn = str(n)
##        l = len(sn)
##        for m in range(l-1):
##            sn = sn[-1]+sn[:-1]
##            if not isPrime(int(sn)): break
##        else:
##            t += 1
##            print n, t
##print t
