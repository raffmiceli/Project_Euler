from math import *
from operator import *

def fact(x):
    f = 1
    for n in range(2,x+1):
        f = f*n
    return f

def factr(x):
    return reduce(mul, xrange(1,x+1))

def factR(x):
    if x < 0: return None
    if x <= 1: return 1
    else: return x*factR(x-1)

def factSum(n):
    #f = str(fact(n))
    #f = str(factorial(n))
    #f = str(factr(n))
    f = str(factR(n))
    t = 0
    for a in f:
        t += int(a)
    return t

def factSumR(n):
    #return sum([int(i) for i in str(reduce(mul, xrange(1,n+1)))])
    return sum([int(i) for i in str(reduce(lambda x,y: x*y, xrange(1,n+1)))])

def factSumM(n):
    return sum(map(int, str(fact(n))))

print factSum(100)


