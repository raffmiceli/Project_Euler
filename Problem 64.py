from decimal import *
from time import *
d = Decimal
getcontext().prec = 300

def cf(m):
    if not m**.5%1: return []
    n = d(m)**d(.5)
    cf = []
    c = 2*int(n)
    while True:
        n = 1/(n%1)
        frac.append(int(n))
        if int(n) == c:
            return frac

def cflodd(m):
    t = 0
    for n in xrange(m):
        lcf = len(CF(n))
        if lcf%2:
            #print n, lcf
            t += 1
    return t

def CF(s):
    m,d,a0 = 0,1,int(s**.5)
    if not s**.5%1: return []
    a,c,frac = a0,2*a0,[]
    while True:
        m = d*a-m
        d = (s-m**2)/d
        a = (a0+m)/d
        frac.append(a)
        if a == c: return frac

def CFLodd(m):
    return sum(len(CF(n))%2 for n in xrange(m))

start = time()
print CFLodd(10000)
print time()-start

def CFsq(s):
    m,d,a0 = 0,1,int(s**.5)
    if not s**.5%1: return []
    a,c,frac = a0,2*a0,[a0,[]]
    while True:
        m = d*a-m
        d = (s-m**2)/d
        a = (a0+m)/d
        frac[1].append(a)
        if a == c: return frac
