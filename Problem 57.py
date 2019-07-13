def rt2ex(n):
    def dec(n):
        if n == 0: return 0.5
        else: return 1/(2+dec(n-1))
    return 1+dec(n)

def root2(n):
    r = 0.5
    for a in range(n-1):
        r = 1/(2+r)
    return 1+r

def numcount(n):
    a,b,count = 1,1,0
    for m in range(n):
        a,b = a+2*b,a+b
        if len(str(a)) > len(str(b)):
            count += 1
    return count

print numcount(1000)

def numCount(n):
    return 2*int((n-1)/13.0)+1

def NumCount(n):
    i,x = 0,0
    while i < n-1:
        i,x = i+13,x+2
    return x-1
