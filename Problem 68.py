from itertools import *
from operator import *

##outer = range(6,11)
##bucket = []
##for p in permutations(range(1,11)):
##    if sorted(p[:5]) == outer and p[0] == 6:
##        a = [p[0],p[5],p[6]]
##        s = sum(a)
##        b = [p[1],p[6],p[7]]
##        if sum(b) == s:
##            c = [p[2],p[7],p[8]]
##            if sum(c) == s:
##                d = [p[3],p[8],p[9]]
##                if sum(d) == s:
##                    e = [p[4],p[9],p[5]]
##                    if sum(e) == s: 
##                        joint = ''.join(map(str,a+b+c+d+e))
##                        bucket.append(int(joint))
##                        #print int(joint)
##print max(bucket)

bucket = []
for o in permutations(range(7,11)):
    o = (6,)+o
    for i in permutations(range(1,6)):
        ngon = [[o[n],i[n-5],i[n-4]] for n in range(5)]
        sums = [sum(line) for line in ngon]
        if len(set(sums)) == 1:
            bucket.append(reduce(add,[''.join(map(str,a)) for a in ngon]))
print max(bucket)
