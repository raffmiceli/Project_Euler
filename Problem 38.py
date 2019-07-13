maxi = 0
check = ['1','2','3','4','5','6','7','8','9']
for n in xrange(10000):
    strn = str(n)
    m = 2
    while len(strn) < 9:
        strn = strn+str(n*m)
        m += 1
    if sorted(strn) == check:
        print n, int(strn)
        if int(strn) > maxi:
            maxi = int(strn)
print maxi

for n in xrange(9999,0,-1):
    strn = str(n)
    m = 2
    while len(strn) < 9:
        strn = strn+str(n*m)
        m += 1
    if sorted(strn) == check:
        print n, int(strn)
        break
    
