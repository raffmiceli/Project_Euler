def divsum(x):
    s = set([1])
    for n in xrange(2,int(x**.5)+1):
        if not x%n:
            s.add(n); s.add(x/n)
    return sum(s)

##def amichain(n):
##    chain = [n]
##    while True:
##        n = divsum(n)
##        if n == chain[0]: break
##        if n in chain: break
##        if n == 1: break
##        chain.append(n)
##    return chain

##lim = 10**6
##divlist = [0]*lim
##for i in xrange(1,lim):
##    for j in xrange(2*i,lim,i):
##        divlist[j] += i

divdict = {n:divsum(n) for n in xrange(10**6)}
print 'divlist complete'
best = 0
bestcl = 0
for n in xrange(lim):
    chain = [n]
    s = n
    while True:
        s = divdict[s]
        if s == 1: break
        if s > lim: break
        if s == n: break
        if s in chain: break
        chain.append(s)
    if chain[0] == divdict[chain[-1]]:
        if len(chain) > bestcl:
            bestcl = len(chain)
            best = min(chain)
print best, bestcl
