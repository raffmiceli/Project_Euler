from gmpy2 import *

np = 0
n = 1
s = 2
nd = 5
side = 3
while True:
    for a in xrange(1,4):
        n += s
        if is_prime(n): np += 1
    if float(np)/nd < 0.1:
        print side
        break
    n += s
    s += 2
    nd += 4
    side += 2

stop = 0.1
n = 3
np = 0
start = time()
while True:
    for i in xrange(1,4):
        if is_prime(n**2-i*(n-1)):
            np += 1
    if float(np)/(2*n-1) < stop:
        print n
        break
    n += 2
