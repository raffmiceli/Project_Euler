from time import *

def part(m):
    def pent(n): return n*(3*n-1)/2

    def gpent(n):
        if n%2: return pent(-(n/2)-1)
        else: return pent(n/2+1)

    gpents = [gpent(n) for n in xrange(int(m**.5))]
    p = [1]
    n = 1
    si = [1,1,-1,-1]
    while True:
        r,i = 0,0
        while True:
            k = gpents[i]
            if k > n: break
            r += si[i%4]*p[n-k]
            i += 1
        p.append(r)
        #print n, p[-1]
        if not p[-1]%m:
            return n, p[-1]
        n += 1

start = time()
print part(10**6)
print time()-start

##def P(n):
##    if n<0: return 0
##    if PN[n]: return PN[n]
##    total = 0
##    for k in range(1,int(n**.5)+1):
##        pn1, pn2 = P(n - k*(3*k+1)/2), P(n - k*(3*k-1)/2)
##        total += pn1+pn2 if k%2 else -pn1-pn2
##    PN[n] = total % 1000000
##    return PN[n]
##
##PN = [0]*100000
##PN[0] = 1
##i = 1
##while P(i): i+=1
##print i
