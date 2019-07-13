from math import *

def quad(a, b, c):
    pos = (-b+sqrt(b**2-4*a*c))/(2*a)
    return pos

def tri(n): return n*(n+1)/2
def pent(n): return n*(3*n-1)/2
def hexa(n): return n*(2*n-1)

def istri(n):
    r = quad(1.0,1.0,2.0*n)
    if not r%1: return True
    else: return False

def ispent(n):
    r = quad(3.0,-1.0,-2.0*n)
    if not r%1: return True
    else: return False

def ishexa(n):
    r = quad(2.0,-1.0,-n)
    if not r%1: return True
    else: return False

for n in range(1,100001):
    t = tri(n)
    if ispent(t) and ishexa(t):
        print n, t
