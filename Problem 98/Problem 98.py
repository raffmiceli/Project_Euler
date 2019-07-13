words = open('words.txt','r').read().replace('"','').split(',')
sqlist = [['0']]+[[str(n**2) for n in xrange(int((10**m)**.5), \
                int((10**(m+1))**.5)+1)] for m in xrange(9)]
for n in xrange(2,9,2): sqlist[n] = sqlist[n][1:-1]

wordict = {}
for word in words:
    ssw = ''.join(sorted(word))
    if wordict.has_key(ssw):
        wordict[ssw].append(word)
    else: wordict[ssw] = [word]
for key in wordict.keys():
    if len(wordict[key]) == 1:
        del wordict[key]
pairs = wordict.values()

bestsq = 0
for pair in pairs:
    p1,p2 = pair[0],pair[1]
    le,les,dup = len(p1),len(set(p1)),0
    if les != le:
        ds,dup = [],1
        for n in xrange(le):
            if p1.count(p1[n]) > 1: ds.append(n)
    for sq in sqlist[le]:
        if len(set(sq)) == les:
            if dup and (sq[ds[0]] != sq[ds[1]]): continue
            numdict = {p1[n]:sq[n] for n in xrange(le)}
            test = ''.join([numdict[c] for c in p2])
            if test in sqlist[le]:
                msq = max(int(sq),int(test))
                bestsq = max(bestsq,msq)
print bestsq
