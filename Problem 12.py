from math import *
from datetime import datetime

def triNum(x):
    e = 1
    c = 0
    
    while e <= x:
        c += e
        e += 1
    return c

def triN(n):
    return n*(n+1)/2

def numFacts(x):
    c = 2
    s = int(sqrt(x))
    for e in xrange(2,s+1):
        if x%e == 0: c+=2
    if s**2 == x: c -= 1
    return c


def triDiv1(n):
    t = 1
    k = 0
    x = 1
    c = 1
    while True:
        f = numFacts(x)

        #if f > k:
            #k = f
            #print t, x, f
            
        if f > n: break
        c += 1
        x += c
        t += 1
        
    return x

#print triDiv1(500)

def triDiv2(n):
    x = 1
    while True:
        f = numFacts(x*(x+1)/2)
        if f > n: return x, x*(x+1)/2
        x += 1

#print triDiv2(500)

start = datetime.now()
triDiv1(500)
print datetime.now()-start
start = datetime.now()
triDiv2(500)
print datetime.now()-start

