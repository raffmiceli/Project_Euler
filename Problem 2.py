def fibonacci(e):
    fibs = [0,1]
    while fibs[-1] < e:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:-1]

t = 0
for n in fibonacci(4000000):
    if n%2 == 0: t += n
print t

def fibsum(n):
    return sum([i for i in fibonacci(n) if i%2==0])
