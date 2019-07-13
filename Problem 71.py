from operator import *
from time import *

def farey(n):
    seq = [(0,1),(1,1)]
    for a in xrange(2,n+1):
        b = 0
        while b < len(seq)-1:
            if seq[b][1]+seq[b+1][1] == a:
                num = seq[b][0]+seq[b+1][0]
                den = seq[b][1]+seq[b+1][1]
                seq.insert(b+1,(num,den))
            b += 1
    return seq

def gcd(a,b):
    if a == b: return a
    start = min(a,b)
    t = a
    while t != 1:
        if not b%t and not a%t:
            return t
        t -= 1
    return t

def tleft37(n):
    p,q,t = 2,5,0
    while t <= n:
        if t == q+7:
            p += 3
            q += 7
        t += 1
    return (p,q)

#print tleft37(1000000)

def Tleft37(n):
    p = (n/7-1)*3+2
    q = (n/7-1)*7+5
    return (p,q)

print Tleft37(1000000)

def TLeft37(n):
    a,b = 2,5
    while b+7 < n:
        a,b = a+3,b+7
    return (a,b)

#print TLeft37(1000000)

def fareygen(n):
    a,b = 0,1
    yield (a,b)
    c,d = 1,n
    yield (c,d)
    while d != 1:
        p = ((n+b)/d)*c-a
        q = ((n+b)/d)*d-b
        a,b = c,d
        c,d = p,q
        yield (p,q)
