from time import *

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

def pellsol(d):
    a0 = int(d**.5)
    cf = CF(d)
    a = [0,0,a0]+cf
    p = [0,1,a0]
    q = [1,0,1]
    n = 3
    while True:
        if p[-1]**2-d*q[-1]**2 == 1:
            return (p[-1],q[-1])
        p.append(a[n]*p[n-1]+p[n-2])
        q.append(a[n]*q[n-1]+q[n-2])
        #print (p[-1],q[-1])
        if n == len(a)-1: a += cf
        n += 1

def pellSol(d):
    n1,d1,n2,d2 = 0,1,1,0
    while True:
        a = n1+n2
        b = d1+d2
        t = a**2 - d*b**2
        #print (a,b)
        if t == 1: return (a,b)
        if t == 0: return None
        if t > 0: n2,d2 = a,b
        else: n1,d1 = a,b

def pellmaxx(lim):
    md,mpq = 0,(0,0)
    for d in [n for n in xrange(lim) if n**.5%1]:
        pq = pellsol(d)
        if pq[0] > mpq[0]:
            md,mpq = d,pq
            #print d, pq
    return md#, mpq

#print pellmaxx(1000)

def pellsols(n,l):
    pq = pellsol(n)
    x1 = pq[0]
    y1 = pq[1]
    x = [x1]
    y = [y1]
    while len(x) < l:
        x.append(x1*x[-1]+n*y1*y[-1])
        y.append(x1*y[-1]+y1*x[-2])
    return zip(x,y)

#print pellsols(7,7)

##def cfraction(sr):
##    def next(pv, v, n): return v, v*n + pv
##    srm = int(sr**.5)
##    px, py = 1, 0
##    x, y = srm, 1
##    a, b = 1, srm
##    while True:
##        a = (sr - (b**2)) / a
##        n = (srm + b) / a
##        b = -(b - n*a)
##        px, x = next(px, x, n)
##        py, y = next(py, y, n)
##        yield x, y
##
##def problem066(limit = 1000):
##    l = {}
##    for d in range(2, limit+1):
##        if d**0.5 % 1 == 0: continue
##        for x, y in cfraction(d):
##             if x**2 - d*y**2 == 1: break
##        l[int(x)] = d
##    return l[max(l)]
##
##print problem066()

##res, maxx = 0, 0
##for D in xrange(2, 10001):
##   a0 = int(D**.5)
##   if a0*a0 == D: continue
##   m, d, a = 0, 1, a0
##   num, den = a, 1
##   nnum, nden = 1, 0
##   while num**2-D*den**2 != 1:
##      m = d*a-m
##      d = (D-m*m)/d
##      a = int((a0+m)/d)
##      num, nnum = a*num+nnum, num
##      den, nden = a*den+nden, den
##   if num > maxx:
##      maxx, res = num, D
##print res
