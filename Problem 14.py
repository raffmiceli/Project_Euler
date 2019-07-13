def cstI(x):
    c = 1
    while x != 1:
        if x%2: x = 3*x+1
        else: x /= 2
        c += 1
    return c

def cstR(n):
    if n == 1: return 0
    if n%2: return cstR(3*n+1)+1
    else: return cstR(n/2)+1

def csts(n):
    b,d = 0,0
    for x in xrange(n/2+1,n,2):
        c = cstI(x)
        if c > d:
            #print x, c
            b,d = x,c
    print b,d

def cstMEM(x):
    sts = {1:0}
    def cstH(n):
        if not sts.has_key(n):
            if n%2: sts[n] = cstH(3*n+1)+1
            else: sts[n] = cstH(n/2)+1
        return sts[n]
    for n in range(1,x,2):
        cstH(n)
    print sts.keys()[sts.values().index(max(sts.values()))]

def cstsT(n):
    b,d = 0,0
    tried = set()
    for x in xrange(1,n+1,2):
        c = 1
        a = x
        if x in tried: continue
        while x > 1:
            tried.add(x)
            if x%2: x = 3*x+1
            else: x /= 2
            c += 1
        if c > d:
            b = a
            d = c
    print b,d
