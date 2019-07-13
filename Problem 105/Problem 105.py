from itertools import combinations

def isSpecialSumSet(s):
    uSet = set(s)
    for i in range(2,len(s)):
        maxSet = max(uSet)
        for a in combinations(s, i):
            ss = sum(a)
            if ss <= maxSet or ss in uSet: return False
            else: uSet.add(ss)
    return True

t = 0
c = 1
for line in open('sets.txt'):
    s = [eval(n) for n in line.split(',')]
    if isSpecialSumSet(s):
        t += sum(s)
    print "Done with set",c
    c += 1
print t
