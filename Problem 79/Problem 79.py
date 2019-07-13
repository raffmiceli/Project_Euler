from itertools import *

f = open('keylog.txt', 'r')
codes = [c[:-1] for c in f.readlines()]
f.close()
codes =  sorted(list(set(codes)))
print codes
##73162890

def codefind1(codes):
    code = ''
    while True:
        test = ''
        for c in codes:
            if len(c) != 1:
                test += c[1]
        m = ''
        for c in codes:
            if c[0] not in test:
                m = c[0]
                break
        code += m
        codes = [c[1:] if c[0] == m else c for c in codes]
        codes = [c for c in codes if len(c) != 0]
        if len(codes) == 0: break
    return code

#print codefind1(codes)

def codefind2(codes):
    code = ''
    while True:
        array = [0]*10
        for c in codes:
            array[int(c[0])] += 1
        #print array
        m = str(array.index(max(array)))
        code += m
        codes = [c[1:] if c[0] == m else c for c in codes]
        codes = [c for c in codes if len(c) != 0]
        #print codes
        if len(codes) == 0: break
    return code

#print codefind2(codes[1:])

def codefind3(codes):
    d = set()
    for code in codes:
        for c in code:
            d.add(c)
    d = list(d)
    for i in range(len(d)):
        for j in range(i+1, len(d)):
            for c in codes:
                if d[i] in c and d[j] in c:
                    if c.index(d[i]) > c.index(d[j]):
                        d[i], d[j] = d[j], d[i]
                        break
    return ''.join(digits)

#print codefind3(codes)

def codefind4(codes):
    d = set()
    for code in codes:
        for c in code:
            d.add(c)
    perms = permutations(d)
    for p in perms:
        ps = ''.join(p)
        for c in codes:
            if not (ps.index(c[0]) < ps.index(c[1]) < ps.index(c[2])):
                break
        else: return ps

#print codefind4(codes)
