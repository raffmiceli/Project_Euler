def sdce(n):
    chain = [n]
    while True:
        n = sum(int(c)**2 for c in str(n))
        chain.append(n)
        if n in [1,89]:
            return n
c89 = []
c1 = []
for n in xrange(1,7*81+1):
    if sdce(n) == 89:
        c89.append(n)
    else: c1.append(n)
#print c1
n = 1
t = 0
while n < 10**7:
    if not n%100000: print n
    s = sum(int(c)**2 for c in str(n))
    if s in c1:
        n += 1
        continue
    else: t += 1
    n += 1
print t

#8581146

def SquareSum(n):
    k = 0
    while n:
        m = n % 10
        n = n/10
        k = k + m*m
    return k

def Compute(ndigits):
    def Recurse(n):
        if not d.has_key(n):
            d[n] = Recurse(SquareSum(n))
        return d[n]
    max = 10**ndigits
    d = {1:1, 89:89}
    for i in range(1, 9*9*ndigits+1):
        Recurse(i)
    count = {1:0, 89:0}
    ss = {}
    us = {}
    sums = {}
    for i in range(0,10):
        ss[i] = i * i
        us[i] = 1
        sums[i*i] = i
    
    m = 10
    while m < max:
        vs = us.keys()
        lus = us.copy()
        for i in range(1, 10):
            n = i * m
            for v in vs:
                k = ss[i] + ss[v]
                if not sums.has_key(k):
                    sums[k] = n + v
                    us[n+v] = lus[v]
                    ss[n+v] = k
                else:
                    us[sums[k]] = us[sums[k]] + lus[v]
        m = m * 10
    del us[0]
    for i,n in us.items():
        k = d[ss[i]]
        count[k] = count[k] + n
    return count[89]

##ndict = {n:0 for n in xrange(10**7)}
##n = 1
##found = set()
##while 0 in ndict.values():
##    print n
##    if '0' in str(n):
##        ndict[n] = ndict[int(str(n).replace('0',''))]
##        n += 1
##        continue
##    if n in found:
##        n += 1
##        continue
##    c = sdc(n)
##    for i in c:
##        ndict[i] == c[-1]
##        found.add(i)
##    n += 1
##print ndict.values().count(89)

##ndict = {n:0 for n in xrange(10**7)}
##n = 1
##while 0 in ndict.values():
##    if ndict[n]:
##        n += 1
##        continue
##    s = n
##    chain = [n]
##    while True:
##        s = sum(int(c)**2 for c in str(s))
##        if ndict[s] != 0:
##            for m in chain:
##                ndict[m] = ndict[s]
##            break
##        if s in [1,89]:
##            for m in chain:
##                ndict[m] = s
##            break
##        chain.append(s)
##    print ndict[n]
##    n += 1
##print ndict.values().count(89)
