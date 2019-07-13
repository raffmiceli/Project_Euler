terms = []
for n in xrange(2,101):
    for m in xrange(2,101):
        a = n**m
        if a not in terms:
            terms.append(a)
print len(terms)

def numpows(x):
    terms = set()
    nums = xrange(2,x+1)
    for n in nums:
        for m in nums:
            terms.add(n**m)
    return len(terms)

def numPows(x):
    return len(set(n**m for n in xrange(2,x+1) for m in xrange(2,x+1)))
    
