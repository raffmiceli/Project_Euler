from math import factorial as f

def fact(x):
    t = 1
    for n in range(1,x+1):
        t = t*n
    return t

true = [] 

for n in range(50000):
    t = 0
    for l in str(n):
        t += fact(int(l))
        if t > n: break
    else:
        if t == n and n > 2:
            true.append(n)
            print n

print true, sum(true)

true = []

for n in xrange(3,50000):
    t = sum(f(int(l)) for l in str(n))
    if t == n: true.append(n)
print true, sum(true)

print sum(n for n in xrange(3,50000) if sum(f(int(l)) for l in str(n)) == n)
