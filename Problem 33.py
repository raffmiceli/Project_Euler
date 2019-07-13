from fractions import Fraction as f
from operator import *

true1 = set([])
true2 = set([])

for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if float(10*b+a)/(10*a+c) == float(b)/c and a != b:
                st = str(b)+str(a)+'/'+str(a)+str(c)
                true1.add(st)
                true2.add(float(b)/c)

t = reduce(mul, true2)
print list(true1), [str(f(n)) for n in true1], f(str(t))

##true1 = []
##true2 = []
##for a in range(1,10):
##    for b in range(1,10):
##        for c in range(1,10):
##            if float(10*b+a)/(10*a+c) == float(b)/c and a != b:
##                st = str(b)+str(a)+'/'+str(a)+str(c)
##                if st not in true1:
##                    true1.append(st)
##                    true2.append(float(b)/c)
##t = 1
##
##for n in true2:
##    t = t*n
##
##print true1, t
                
