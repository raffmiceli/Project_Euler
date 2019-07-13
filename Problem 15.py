from math import *

def fact(x):
    f = 1
    for n in range(2,x+1):
        f = f*n
    return f

def Comb(n,k):
    return fact(n)/(fact(k)*fact(n-k))

def Paths(n):
    return fact(2*n)/fact(n)**2

print Comb(40,20)
print Paths(20)
