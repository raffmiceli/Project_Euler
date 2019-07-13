from math import *

def divsum(x):
    #divs = []
    s = 1
    for n in xrange(2,(x/2)+1):
        if not x%n:
            #divs.append(n)
            s += n
    #return sum(divs)
    return s

def divSum(x):
    s = 1
    for n in xrange(2, int(sqrt(x))+1):
        if not x%n:
            s += n+x/n
        if n == sqrt(x): s -= n
    return s

def divsSum(x):
    s = set([1])
    for n in xrange(2,int(sqrt(x))+1):
        if not x%n:
            s.add(n); s.add(x/n)
    return sum(s)

def amicSum(n):
    amsum = 0
    #amics = []
    for n in xrange(1,n+1):
        m = divSum(divSum(n))
        if n == m and n != divSum(n):
            amsum += n
            #print n
    #return sum(amics)
    return amsum

def amicsum(n):
    if n < 284: return 0
    found = []
    amsum = 0
    for n in xrange(284,n+1):
        if n in found: continue
        d = divsum(n)
        if n == d: continue
        m = divsum(d)
        if n == m:
            amsum += n+d
            found.append(n)
            found.append(d)
    return amsum

def sumdiv(x):
    return 1 + sum(n+x/n for n in xrange(2,int(x**0.5)+1) if not x%n)

def sumDiv(x):
    return sum(n for n in xrange(1,x/2+1) if not x%n)

def sumamic(x):
    return sum(n for n in xrange(1,x) if n==sumdiv(sumdiv(n)) and n!=sumdiv(n))
