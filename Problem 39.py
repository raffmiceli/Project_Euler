from math import *

##maxi = 0
##maxin = 0
##maxil = []
##for n in xrange(120,1000,2):
##    truel = []
##    true = 0
##    for a in xrange(n/2):
##        for b in xrange(a,n/2):
##            c = sqrt(a**2+b**2)
##            if a+b+c == n:
##                t = sorted([a,b,int(c)])
##                if t not in truel:
##                    truel.append(t)
##                    true += 1
##    print n, true
##    if true > maxi:
##        maxi = true
##        maxin = n
##        maxil = truel
##
##print maxin, maxi, maxil

maxi,maxin,maxil = 0,0,[]
for n in xrange(2,1000,2):
    truel = []
    true = 0
    a,b = 1,1
    while a <= b:
        b = float(n*(n-2*a))/(2*(n-a))
        if b > 0 and not b%1:
            true += 1
            truel.append((a,int(b),int(sqrt(a**2+b**2))))
        a += 1
    #print n, true
    if true > maxi:
        maxi,maxin,maxil = true,n,truel
print maxin, maxi, maxil

##k = []
##for a in xrange(3,501):
##    for b in xrange(a,501):
##        if not sqrt(a**2 + b**2)%1:
##            p = a + b + int((a**2 + b**2)**0.5)
##            k.append(p)
##c = 0
##for i in xrange(1000):
##    if k.count(i) > c:
##        c = k.count(i)
##        print i, c

def gcd(a,b):
    while a:
        a,b = b%a,a
    return b

def irtm(x):
    lim = int(x**.5)+1
    lar = [0]*(x+1)
    for n in xrange(1,lim):
        for m in xrange(n+1,lim,2):
            if gcd(m,n) == 1:
                a = m**2-n**2
                b = 2*m*n
                c = m**2+n**2
                L = a+b+c
                if L > x: break
                for y in xrange(1,x/L+1):
                    lar[y*L] += 1
    return lar.index(max(lar))

print irtm(1000)
