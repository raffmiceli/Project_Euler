from itertools import *

def minCheck(n):
    t = 0
    l = set(range(n))
    for m in range(2,n/2+1):
        for a in combinations(l,m):
            for b in combinations(l-set(a),m):
                if all(b[i] > a[i] for i in range(m)) or \
                   all(a[i] > b[i] for i in range(m)):
                    continue
                else: t += 1
    return t/2

print minCheck(12)
