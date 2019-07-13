def gcd(a,b):
    while a:
        a,b = b%a,a
    return b

def sit(x,z):
    lim = int(x**.5)+1
    lar = [0]*(x+1)
    for n in xrange(1,lim):
        for m in xrange(n+1,lim,2):
            if gcd(m,n) == 1:
                a = m**2-n**2
                b = 2*m*n
                c = m**2+n**2
                L = a+b+c
                if L > x: break
                for y in xrange(1,x/L+1):
                    lar[y*L] += 1
    return lar.count(z)

print sit(1500000,1)
