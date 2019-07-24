# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Brute force with loops.
def ssd1(x):
    ss1 = 0
    ss2 = 0
    for n in range(1,x+1):
        ss1 += n**2
        ss2 += n
    ssd = ss2**2 - ss1
    return ssd

#print ssd1(100)


# Not exactly sure what my goal was here....
#print sum([x**3 for x in range(1,101)]) - sum([x**2 for x in range(1,101)])
#print sum([x for x in range(1,101)])**2 - sum([x**2 for x in range(1,101)])
#print sum(range(101))**2 - sum([n**2 for n in range(101)])
#print sum([x*x*(x-1) for x in range(101)])
#print sum([x**3-x**2 for x in range(101)])

# Quick way using expressions for the sums.
def ssd2(n):
    return (n*(n+1)/2)**2 - n*(n+1)*(2*n+1)/6

#print ssd2(100)
