from math import *

def quad(a, b, c):
    pos = (-b+sqrt(b**2-4*a*c))/(2*a)
    return pos

def pent(n):
    return n*(3*n-1)/2

def ispent(n):
    r = quad(1.0,-1.0/3,(-2.0*n)/3)
    if not r%1: return True
    else: return False

a = 0
b = 0
small = 1000000000

for n in xrange(1,1100):
    for m in xrange(n+1,2200):
        su = pent(n) + pent(m)
        di = pent(m) - pent(n)
        if ispent(su) and ispent(di):
            print n, m, di
            if di < small:
                small = di
                a = n
                b = m
print small

##for n in xrange(1,1100):
##    for m in xrange(n+1,2200):
##        su = pent(n) + pent(m)
##        di = pent(m) - pent(n)
##        if ispent(su) and ispent(di):
##            print n, m, di
##            break
