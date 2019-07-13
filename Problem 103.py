##[20,31,38,39,40,42,45]
##lolwut?
##[39,59,70,77,78,79,81,84]

from itertools import combinations

def isSpeciaSumSet(s):
    uSet = set(s)
    for i in range(2,len(s)):
        maxSet = max(uSet)
        for a in combinations(s, i):
            ss = sum(a)
            if ss <= maxSet or ss in uSet: return False
            else: uSet.add(ss)
    return True

def problem103():   
    for a in range(20,23):
        for b in range(30,35):
            for c in range(b,40):
                for d in range(c,44):
                    for e in range(d,45):
                        for f in range(e,46):
                            for g in range(f,47):
                                if isSpeciaSumSet([a,b,c,d,e,f,g]):
                                    return (a,b,c,d,e,f,g)

print (problem103())
