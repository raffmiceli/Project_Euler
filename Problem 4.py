def revStr(aStr):
    if len(aStr) <= 1: return aStr
    return aStr[-1]+revStr(aStr[1:-1])+aStr[0]

h = 0
for m in range(900,1000):
    for n in range(900,1000):
        mn = m*n
        if str(mn) == str(mn)[::-1]:
            #print m, n, mn
            if mn >= h: h = mn
print h

print max([x*y for x in range(900,1000) for y in range(900,1000) if str(x*y) == str(x*y)[::-1]])
