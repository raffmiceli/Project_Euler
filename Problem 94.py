##lim = 10**9
##m = (lim-1)/3
##t = 0
##n = 5
##while n < m:
##    p = 3*n+1
##    s = p/2.0
##    a = s*(s-n)*(s-n)*(s-(n+1))
##    if is_square(mpz(a)):
##        t += p
##        print n,t
##    p = 3*n-1
##    s = p/2.0
##    a = (s*(s-n)*(s-n)*(s-(n-1)))**.5
##    if not a%1:
##        t += p
##        print n,t
##    n += 2
##print t

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

##l = pellsols(3,30)
##t = 0
##for s in l[1:]:
##    x = s[0]
##    y = s[1]
##    a = (2*x+1)/3.0
##    if not a%1:
##        a = int(a)
##        if 3*a+1 < 10**9:
##            t += 3*a+1
##            #print a,t
##    a = (2*x-1)/3.0
##    if not a%1:
##        a = int(a)
##        if 3*a-1 < 10**9:
##            t += 3*a-1
##            #print a,t
##print t

#snapey1979
a,b,c,n,p,t = 3,4,5,0,0,0
while True:
    p = 4*min(a,b)+c
    if p > 10**9: break
    t += p
    if not n%2: a,b,c = -a+2*b+2*c,-2*a+b+2*c,-2*a+2*b+3*c
    else: a,b,c = a-2*b+2*c,2*a-b+2*c,2*a-2*b+3*c
    n += 1
print t
