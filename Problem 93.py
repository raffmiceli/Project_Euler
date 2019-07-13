from itertools import *
best,bests = 0,''
digs = ['1.0','2.0','3.0','4.0','5.0','6.0','7.0','8.0','9.0']
for t in range(9):
    for u in range(t+1,9):
        for v in range(u+1,9):
            for w in range(v+1,9):
                ints = set([0])
                x = [digs[t],digs[u],digs[v],digs[w]]
                if len(x) != 4: continue
                for s in permutations(x):
                    for p in combinations_with_replacement('+-*/',3):
                        for o in permutations(p):
                            try: a = eval('(('+s[0]+''+o[0]+''+s[1]+')'\
                                          +o[1]+''+s[2]+')'+o[2]+''+s[3]+'')
                            except ZeroDivisionError: a = 0
                            try: b = eval('('+s[0]+''+o[0]+''+s[1]+')'\
                                          +o[1]+'('+s[2]+''+o[2]+''+s[3]+')')
                            except ZeroDivisionError: b = 0
                            for n in [a,b]:
                                if n >= 0 and not n%1:
                                    ints.add(int(n))
                ints = sorted(list(ints))
                m = max(e for e in ints if e == ints.index(e))
                if m > best:
                    best,bests = m,''.join(z[0] for z in x)
print best, bests

##                            try: a = eval(''+s[0]+''+o[0]+''+s[1]+''+o[1]+''+s[2]+''+o[2]+''+s[3]+'')
##                            except ZeroDivisionError: a = 0
##                            try: b = eval('('+s[0]+''+o[0]+''+s[1]+')'+o[1]+'('+s[2]+''+o[2]+''+s[3]+')')
##                            except ZeroDivisionError: b = 0
##                            try: c = eval(''+s[0]+''+o[0]+'('+s[1]+''+o[1]+''+s[2]+')'+o[2]+''+s[3]+'')
##                            except ZeroDivisionError: c = 0
##                            try: d = eval(''+s[0]+''+o[0]+'('+s[1]+''+o[1]+''+s[2]+''+o[2]+''+s[3]+')')
##                            except ZeroDivisionError: d = 0
