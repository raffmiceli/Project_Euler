def ssd1(x):
    ss1 = 0
    ss2 = 0
    for n in range(1,x+1):
        ss1 += n**2
        ss2 += n
    ssd = ss2**2 - ss1
    return ssd

#print ssd1(100)

#print sum([x**3 for x in range(1,101)]) - sum([x**2 for x in range(1,101)])
#print sum([x for x in range(1,101)])**2 - sum([x**2 for x in range(1,101)])
#print sum(range(101))**2 - sum([n**2 for n in range(101)])
#print sum([x*x*(x-1) for x in range(101)])
#print sum([x**3-x**2 for x in range(101)])

def ssd2(n):
    return (n*(n+1)/2)**2 - n*(n+1)*(2*n+1)/6

#print ssd2(100)
