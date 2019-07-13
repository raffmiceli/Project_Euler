from memoize import *

def csums(n):
    cray = [1]+[0]*n
    for i in xrange(1,n+1):
        for j in xrange(i,n+1):
            cray[j] += cray[j-i]
    return cray[-1]-1

print csums(100)

##def csums(n):
##    cs = xrange(1,n)
##    cray = [1]+[0]*n
##    for i in xrange(len(cs)):
##        for j in xrange(cs[i],n+1):
##            cray[j] += cray[j-cs[i]]
##    return cray[n]

##def part(m):
##    def pent(n): return n*(3*n-1)/2
##
##    def gpent(n):
##        if n%2: return pent(-(n/2)-1)
##        else: return pent(n/2+1)
##
##    def s(i):
##        if i%4 < 2: return 1
##        else: return -1
##
##    p = [1]
##    for n in xrange(1,m+1):
##        r,i = 0,0
##        while True:
##            k = gpent(i)
##            if k > n: break
##            r += s(i)*p[n-k]
##            i += 1
##        p.append(r)
##    return p[-1]
##
##print part(100)-1

def p(n,k):
    if n < 0: return 0
    if k == 1: return 1
    return p(n-k,k)+p(n,k-1)

p = memoize(p)

print p(100,99)

