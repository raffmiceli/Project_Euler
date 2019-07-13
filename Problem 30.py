true = []
for n in xrange(2,200000):
    s = 0
    for m in str(n):
        s += int(m)**5
    if s == n:
        print n
        true.append(n)
print sum(true)

print sum(n for n in xrange(2,200000) if sum(int(i)**5 for i in str(n)) == n)
