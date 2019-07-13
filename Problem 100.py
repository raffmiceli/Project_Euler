x,y = [1],[1]
while y[-1] < 10**12:
    xn,yn = x[-1],y[-1]
    x.append(3*xn+2*yn-2)
    y.append(4*xn+3*yn-3)
print x[-1]

##r,b = 35,85
##s1,s2,s3 = 1,6,35
##while r+b < 10**12:
##    s1 = s2
##    s2 = s3
##    s3 = s2*6-s1
##    r = s3
##    b = int(((r**2*8+1)**.5+2*r+1))/2
##    #print r,b,r+b
##print b

##p,q,c = 15,6,3+2*2**.5
##while p+q < 10**12:
##    p = int(p*c)-2
##    q = int(q*c)+1
##print p

##def propdiv(x):
##    divs = set()
##    for n in xrange(1,x/2+1):
##        if not x%n:
##            divs.add(n)
##            divs.add(x/n)
##    return sorted(list(divs))
##
##def tri(n): return n*(n+1)/2

##nn1,nn12 = [],[]
##start = 0
##n = start
##while n < start+10**7:
##    num = n*(n+1)
##    nn1.append(num)
##    nn12.append(num/2)
##    n += 1
##finds = sorted(list(set(nn1).intersection(nn12)))
##sols = []
##sols1 = []
##for n in finds:
##    sols.append(nn1.index(n)+start+1)
##    sols1.append(nn12.index(n)+start+1)
##print sols
##print sols1
