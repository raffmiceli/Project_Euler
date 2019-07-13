t = 0
for n in xrange(1,1001):
    t += n**n
print str(t)[-10:]

print str(sum(x**x for x in xrange(1,1001)))[-10:]
