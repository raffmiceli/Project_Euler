def sumDigits(n):
    t = 0
    for m in str(n):
        t += int(m)
    return t

print sumDigits(2**1000)

def sumD(n):
    return sum([int(i) for i in str(n)])
    #return sum(map(int, str(n)))

print sumD(2**1000)
