from math import factorial as f

fs = [f(n) for n in range(10)]

def fsum(n):
    return sum(fs[int(c)] for c in str(n))

def fseq(n):
    seq = [n]
    while True:
        k = fsum(seq[-1])
        if k in seq: return seq
        seq.append(k)

def ss(n):
    return ''.join(sorted(str(n)))

true = []
truesets = []
for n in xrange(1000000):
    if ss(n) in truesets:
        true.append(n)
        print n, len(true)
        continue
    k = n
    nums = [k]
    while True:
        k = fsum(k)
        if k in nums: break
        nums.append(k)
    if len(nums) == 60:
        true.append(n)
        truesets.append(ss(n))
        print n, len(true)
print true, len(true)

##t = 0
##ts = []
##c = set()
##for n in xrange(1000000):
##    sn = ss(n)
##    if sn in c: continue
##    if sn in ts:
##        t += 1
##        print n, t
##        continue
##    s = fseq(n)
##    if len(s) == 60:
##        t += 1
##        ts.append(sn)
##        print n, t
##        for b in [ss(a) for a in s][1:]:
##            c.add(b)

##print fseq(4079)
##print fseq(1479)
##print fseq(223479)
##
##trig = [367945,367954]
##
##t = 0
##for n in xrange(1000000):
##    if fsum(n) in trig:
##        t += 1
##        print n, t
##print t

##def chain60(n):
##    facs = dict(zip(map(str,range(10)),map(f,range(10))))
##    clen = {169:3,363601:3,1454:3,871:2,45631:2,872:2,45362:2}
##    def chlen(x):
##        if x not in clen: 
##            sf = sum(facs[c] for c in str(x))
##            if sf == x: clen[x] = 1
##            else: clen[x] = 1 + chlen(sf)
##        return clen[x]
##    t = 0
##    for x in xrange(n):
##        if chlen(x) == 60: t += 1
##    return t
##
##print chain60(1000000)
