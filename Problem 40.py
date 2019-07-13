st = ''
n = 1
while len(st) < 1000000:
    st += str(n)
    n += 1
t = 1
for n in xrange(7):
    a = int(st[10**n-1])
    t *= a
    print a
print t

##from operator import mul
##def PE40(x):
##    def s(k):
##        return (10**k*(9*k-1)+1)/9
##    def d(n):
##        k=0
##        while 1:
##            if s(k+1)>=n: break
##            k=k+1
##        k=k+1
##        num,rem = 10**(k-1)+(n-s(k-1))//k-1, (n-s(k-1))%k
##        if rem==0: return int(str(num)[-1])
##        else: return int(str(num+1)[rem-1])
##    return reduce(mul,[d(10**i) for i in range(x)])
    
    
