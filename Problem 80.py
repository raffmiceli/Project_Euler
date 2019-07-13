from decimal import *
d = Decimal
getcontext().prec = 110

def sumdec(n):
    if not n**.5%1: return 0
    rd = str(d(n).sqrt()).replace('.','')
    #print rd
    return sum(int(a) for a in rd[:100])

print sum(sumdec(n) for n in range(1,101))

##t = 0
##for n in range(1,101):
##    s = sumdec(n)
##    t += s
##    print n, s, t

##def euler80():
##    total = 0
##    for s in xrange(2,100):
##        if s in [4,9,16,25,36,49,64,81]:
##            continue
##        yprev = (s*10L**101)/2
##        s = s * 10L**202
##        y = (s/yprev + yprev)/2
##        while y != yprev:
##            yprev, y = y, (s/y+y)/2
##        total += sum(int(x) for x in str(y)[:100])
##    print total
##
##euler80()

def sqrt(a):
   p = a
   e = a/2
   while e < p:
      p, e = e, (e+a/e)/2
   return p

print sum(sum(int(c) for c in str(sqrt(n*10**200))[:100]) for n in range(1,101) if n**.5%1)
    
