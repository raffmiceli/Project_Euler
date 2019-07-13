from numpy import *

def npoly(n):
    return 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10

x = range(1,12)
y = [npoly(n) for n in x]
#print x
#print y

fits = []
for n in range(1,11):
    coeffs = polyfit(x[:n],y[:n],deg = n-1)
    coeffs = [int(round(b)) for b in coeffs]
    #print coeffs
    m,fit = n-1,0
    for a in coeffs:
        fit += a*(n+1)**m
        m -= 1
    #print n, fit
    fits.append(fit)
print sum(fits)

##fits = []
##for n in range(1,11):
##    fit = 0
##    for j in range(1,n+1):
##        t1,t2 = 1,1
##        for k in range(1,n+1):
##            if j == k: continue
##            t1 *= (n+1)-k
##            t2 *= j-k
##        fit += t1*y[j-1]/t2
##    fits.append(fit)
###print fits
##print sum(fits)


