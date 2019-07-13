from pyprimes import *
from gmpy2 import *
from operator import *

def div(n):
    divs = []
    for m in range(2,int(n**.5)+1):
        if not n%m:
            divs.append(m)
            divs.append(n/m)
    return sorted(set(divs))

##vdict = {n:[] for n in xrange(12001)}
##for n in xrange(4,24001):
##    if isprime(n): continue
##    a = factors(n)
##    l = len(a)
##    for m in xrange(1,l):
##        a1 = a[:-m]
##        a2 = a[-m:]
##        s1 = sum(a1)+reduce(mul,a2)
##        s2 = reduce(mul,a1)+reduce(mul,a2)
##        v1 = (l-m+1)+(n-s1)
##        v2 = 2+n-s2
##        if v1 <= 12000:
##            vdict[v1].append(n)
##        if v2 <= 12000:
##            vdict[v2].append(n)
##        a1 = a[m:]
##        a2 = a[:m]
##        s1 = sum(a1)+reduce(mul,a2)
##        s2 = reduce(mul,a1)+reduce(mul,a2)
##        v1 = (l-m+1)+(n-s1)
##        v2 = 2+n-s2
##        if v1 <= 12000:
##            vdict[v1].append(n)
##        if v2 <= 12000:
##            vdict[v2].append(n)
##print sum(set(min(vdict[n]) for n in xrange(2,12001)))
##for n in xrange(2,12001):
##    print n, min(vdict[n])

##def mprodsum(n):
##    val = []
##    for a in xrange(2,2*n):
##        for b in xrange(a,2*n):
##            if a*b > 2*n: break
##            if (n-2)+a+b == a*b:
##                val.append(a*b)
##            for c in xrange(b,2*n):
##                if a*b*c > 2*n: break
##                if (n-3)+a+b+c == a*b*c:
##                    val.append(a*b*c)
##                for d in xrange(c,2*n):
##                    if a*b*c*d > 2*n: break
##                    if (n-4)+a+b+c+d == a*b*c*d:
##                        val.append(a*b*c*d)
##                    for e in xrange(d,2*n):
##                        if a*b*c*d*e > 2*n: break
##                        if (n-5)+a+b+c+d+e == a*b*c*d*e:
##                            val.append(a*b*c*d*e)
##    return min(val)
##s = set()
##for n in xrange(2,13):
##    a =  mprodsum(n)
##    print n,a
##    s.add(a)
##print sum(s)

vdict = {n:[] for n in xrange(12001)}
m = 24000
for a in xrange(2,m/2):
    for b in xrange(a,m/(a)):
        v = (a*b)-(a+b)+2
        if v <= 12000: vdict[v].append(a*b)
        for c in xrange(b,m/(a*b)):
            v = (a*b*c)-(a+b+c)+3
            if v <= 12000: vdict[v].append(a*b*c)
            for d in xrange(c,m/(a*b*c)):
                v = (a*b*c*d)-(a+b+c+d)+4
                if v <= 12000: vdict[v].append(a*b*c*d)
                for e in xrange(d,m/(a*b*c*d)):
                    v = (a*b*c*d*e)-(a+b+c+d+e)+5
                    if v <= 12000: vdict[v].append(a*b*c*d*e)
                    for f in xrange(e,m/(a*b*c*d*e)):
                        v = (a*b*c*d*e*f)-(a+b+c+d+e+f)+6
                        if v <= 12000: vdict[v].append(a*b*c*d*e*f)
                        for g in xrange(f,m/(a*b*c*d*e*f)):
                            v = (a*b*c*d*e*f*g)-(a+b+c+d+e+f+g)+7
                            if v <= 12000: vdict[v].append(a*b*c*d*e*f*g)
                            for h in xrange(g,m/(a*b*c*d*e*f*g)):
                                v = (a*b*c*d*e*f*g*h)-(a+b+c+d+e+f+g+h)+8
                                if v <= 12000: vdict[v].append(a*b*c*d*e*f*g*h)
                                for i in xrange(h,m/(a*b*c*d*e*f*g*h)):
                                    v = (a*b*c*d*e*f*g*h*i)-(a+b+c+d+e+f+g+h+i)+9
                                    if v < 12000: vdict[v].append(a*b*c*d*e*f*g*h*i)
                                    for j in xrange(h,m/(a*b*c*d*e*f*g*h*i)):
                                        v = (a*b*c*d*e*f*g*h*i*j)-(a+b+c+d+e+f+g+h+i+j)+10
                                        if v < 12000: vdict[v].append(a*b*c*d*e*f*g*h*i*j)
                                        for k in xrange(h,m/(a*b*c*d*e*f*g*h*i*j)):
                                            v = (a*b*c*d*e*f*g*h*i*j*k)-(a+b+c+d+e+f+g+h+i+j+k)+11
                                            if v < 12000: vdict[v].append(a*b*c*d*e*f*g*h*i*j*k)
print sum(set(min(vdict[n]) for n in xrange(2,12001)))

vdict = {n:[] for n in xrange(12001)}
m = 24000
n = 12000
for a in xrange(2,m/2):
    for b in xrange(a,m/a):
        l = [a,b]
        p = reduce(mul,l)
        s = sum(l)
        v = p-s+2
        if v <= n: vdict[v].append(p)
        for c in xrange(b,m/p):
            l = [a,b,c]
            p = reduce(mul,l)
            s = sum(l)
            v = p-s+3
            if v <= n: vdict[v].append(p)
            for d in xrange(c,m/p):
                l = [a,b,c,d]
                p = reduce(mul,l)
                s = sum(l)
                v = p-s+4
                if v <= n: vdict[v].append(p)
                for e in xrange(d,m/p):
                    l = [a,b,c,d,e]
                    p = reduce(mul,l)
                    s = sum(l)
                    v = p-s+5
                    if v <= n: vdict[v].append(p)
                    for f in xrange(e,m/p):
                        l = [a,b,c,d,e,f]
                        p = reduce(mul,l)
                        s = sum(l)
                        v = p-s+6
                        if v <= n: vdict[v].append(p)
                        for g in xrange(f,m/p):
                            l = [a,b,c,d,e,f,g]
                            p = reduce(mul,l)
                            s = sum(l)
                            v = p-s+7
                            if v <= n: vdict[v].append(p)
                            for h in xrange(g,m/p):
                                l = [a,b,c,d,e,f,g,h]
                                p = reduce(mul,l)
                                s = sum(l)
                                v = p-s+8
                                if v <= n: vdict[v].append(p)
                                for i in xrange(h,m/p):
                                    l = [a,b,c,d,e,f,g,h,i]
                                    p = reduce(mul,l)
                                    s = sum(l)
                                    v = p-s+9
                                    if v <= n: vdict[v].append(p)
                                    for j in xrange(h,m/p):
                                        l = [a,b,c,d,e,f,g,h,i,j]
                                        p = reduce(mul,l)
                                        s = sum(l)
                                        v = p-s+10
                                        if v <= n: vdict[v].append(p)
                                        for k in xrange(h,m/p):
                                            l = [a,b,c,d,e,f,g,h,i,j,k]
                                            p = reduce(mul,l)
                                            s = sum(l)
                                            v = p-s+11
                                            if v <= n: vdict[v].append(p)
print sum(set(min(vdict[n]) for n in xrange(2,n+1)))

##Tirian solve

def small_factor_generator(n):
    for i in xrange(2, 1+int(n**.5)):
        if n%i == 0: yield i

def problem088(n=12000):
    best = [0] * (n+1)
    sum_decomp = {}
    for i in xrange(2,2*n+1):
        sum_decomp[i] = set([(1, i)])
        for k in small_factor_generator(i):
            for a,b in sum_decomp[i/k]:
                sum_decomp[i].add((a+1, b+k))
                dex = i+(a+1)-(b+k)
                if dex <= n and best[dex] == 0: best[dex] = i
    return sum(set(best[2:]))

print problem088()

##Orbifold solve

minnumbers = dict((k,-1) for k in range(2,12001))

def Factorizations(n,k=2):
    result = []
    while k*k <= n:
        if n%k == 0:
            result.extend([[k]+f for f in Factorizations(n/k,k)])
        k += 1
    return result + [[n]]

for n in xrange(2,20000):
    for f in Factorizations(n):
        i,j = sum(f),len(f)
        if i <= n:
            k = (n-i)+j
            if k <= 12000 and k >= 2 and minnumbers[k] == -1:
                minnumbers[k] = n

##print len([k for k in minnumbers if minnumbers[k] == -1])
print sum(set(n for k,n in minnumbers.iteritems() if n != -1))

##cantdance solve

N = 12000
s = [ set([]) for i in xrange(2*N+1)]
sol = (N+1)*[0]
count = 0
n = 1
while count < N:
   s[n].add(n-1)
   d = 2
   while d*d <= n:
      if n % d==0:
         for snd in s[n/d]:
            s[n].add(d+snd-1)
      d = d+1
   for i in s[n]:
      if n-i >= 0 and n-i <= N:
         if sol[n-i] == 0:
            sol[n-i] = n
            count = count + 1
         elif sol[n-i] > n:
            sol[n-i] = n
   n = n+1
print sum(set(sol[2:]))

##Kutta solve

def P088(l=12000):
    
    def factors(e, s, plen, ds):
        nplen = plen+1
        for e in xrange(e,l2/s+1):
            ns, nds = s*e, ds+e
            k = nplen + ns - nds
            if k <= l:
                if not array[k]:  
                    array[k] = ns
                else:             
                    array[k] = min(array[k],ns)
                factors(e, ns, nplen, nds)
            
    l2 = l*2
    array = [0]*(l+1)
    for i in xrange(2, l2/2+1):
        factors(i, i, 1, i)
    return sum(set(array))
print P088()
