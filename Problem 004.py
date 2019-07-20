# Problem 4 from Project Euler (projecteuler.net)

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# Recursive function for reversing strings. Kinda pointless since you can just do it with "string_name[::-1]"
def revStr(aStr):
    if len(aStr) <= 1: return aStr
    return aStr[-1]+revStr(aStr[1:-1])+aStr[0]

# Solution with nested for loops
h = 0
for m in range(900,1000):
    for n in range(900,1000):
        mn = m*n
        if str(mn) == str(mn)[::-1]:
            #print m, n, mn
            if mn >= h: h = mn
print h

# Pythonic one-liner solution
print max([x*y for x in range(900,1000) for y in range(900,1000) if str(x*y) == str(x*y)[::-1]])
