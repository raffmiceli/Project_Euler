keep,ka,kb = 0,0,0
for a in xrange(90,100):
    for b in xrange(90,100):
        ds = sum([int(s) for s in str(a**b)])
        if ds > keep:
             ka,kb,keep = a,b,ds
print ka,kb,keep

print max(sum(int(s) for s in str(a**b)) for a in xrange(90,100) for b in xrange(90,100))

print max(sum(int(s) for s in str(num)) for num in set(a**b for a in xrange(90,100) for b in xrange(90,100)))
