from math import *

t = 0
for n in range(1,10):
    for m in range(1,25):
        if len(str(n**m)) == m:
            #print n,m,n**m
            t += 1
print t

##print sum(1 for n in range(1,10) for m in range(1,25) if len(str(n**m)) == m)
##print sum(len(str(n**m)) == m for n in range(1,10) for m in range(1,25))
##print sum(int(1.0/(1-log(n,10))) for n in range(1,10))

##t = 0
##for n in range(1,10):
##    for m in range(1,25):
##        l = len(str(n**m))
##        if l < m: break
##        if l == m:
##            #print n,m,n**m
##            t += 1
##print t
