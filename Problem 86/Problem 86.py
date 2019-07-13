M = 100
t = 0
true = []
for a in xrange(1,M+1):
    for b in xrange(a,M+1):
        for c in xrange(b,M+1):
            if not ((c**2+(a+b)**2)**.5)%1:
                true.append([a,b,c])
                t += 1
print t

##M = 100
##t = 2060
##while True:
##    M += 1
##    print M
##    for a in xrange(1,M+1):
##        for b in xrange(a,M+1):
##            if ((M**2+(a+b)**2)**.5)%1 == 0:
##                t += 1
##    #print t
##    if t > 10**6: break 
##print M

M = 0
t = 0
while True:
    M += 1
    #print M
    for x in xrange(1,2*M):
        if ((M**2+x**2)**.5)%1 == 0:  
            if x < M: t += x/2
            else: t += (x/2)-(x-M)+1
    if t > 10**6: break
print M

def cub(a):
    M = 0
    t = 0
    while M <= a:
        M += 1
        #print M
        for x in xrange(1,2*M):
            if ((M**2+x**2)**.5)%1 == 0:  
                if x < M: t += x/2
                else: t += (x/2)-(x-M)+1
    return t
