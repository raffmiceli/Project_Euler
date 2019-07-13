from math import factorial as f

def C(n,r):
    return f(n)/(f(r)*f(n-r))

fac = [f(n) for n in range(101)]

def C2(n,r):
    return fac[n]/(fac[r]*fac[n-r])

count = 0
for n in range(23,101):
    for r in range(2,n):
        if C(n,r) > 1000000:
            #print n,r
            count += 1
print count

count = 0
for n in range(23,101):
    for r in range(2,n):
        if C(n,r) > 1000000:
            count += n+1-2*r; break
print count
