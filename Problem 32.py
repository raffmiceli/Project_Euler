true = []
s = ['1','2','3','4','5','6','7','8','9']
for a in range(1,100):
    for b in range(123,2000):
        c = a*b
        if sorted(str(a)+str(b)+str(c)) == s:
            if c not in true:
                true.append(c)
                print c, sum(true)

true = set([])
for a in xrange(1,100):
    for b in xrange(123,2000):
        if sorted(str(a)+str(b)+str(a*b)) == s:
            true.add(a*b)
print sum(true)
