from itertools import *

digs = ['0','1','2','3','4','5','6','7','8','9']
squares = ['01','04','09','16','25','36','49','64','81']
combos = [''.join(c) for c in list(combinations(digs,6))]
l = len(combos)
for n in xrange(l):
    if '6' in combos[n] and '9' not in combos[n]:
        combos[n] += '9'; continue
    if '9' in combos[n] and '6' not in combos[n]:
        combos[n] += '6'
t = 0
for a in xrange(l):
    for b in xrange(a+1,l):
        ca = combos[a]; cb = combos[b]
        if all((s[0] in ca and s[1] in cb) \
               or (s[1] in ca and s[0] in cb) \
               for s in squares): t += 1
print t
            
                
