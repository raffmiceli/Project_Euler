# Problem 1 from Project Euler (projecteuler.net)

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# The straightforward, brute force method
t = 0
for n in range(1,1000):
    if n%3 == 0 or n%5 == 0: t += n
print(t)

# No loops, more math-y
def multSum(a, b, n):
    multA = (n-1)/a
    multB = (n-1)/b
    multAB = (n-1)/(a*b)
    multsA = a*multA*(multA+1)/2
    multsB = b*multB*(multB+1)/2
    multsAB = a*b*multAB*(multAB+1)/2
    return multsA + multsB - multsAB

##for n in range(1,21):
##    print(multSum(3,5,10**n))

# Pythonic one-liner function, can solve general problem
def multComp(a,b,n):
    return sum([x for x in range(n) if x%a==0 or x%b==0])
