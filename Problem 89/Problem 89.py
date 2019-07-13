f = open('roman.txt','r')
nums = [s.rstrip('\n') for s in f.readlines()]
f.close()
def NR(n):
    nlist = [['','I','II','III','IV','V','VI','VII','VIII','IX'],\
            ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],\
            ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],\
            ['','M','MM','MMM','MMMM']]
    num = ''
    sn = str(n)[::-1]
    for m in range(len(sn)):
        num = nlist[m][int(sn[m])]+num
    return num

def RN(s):
    t = 0
    rdict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    while len(s) > 0:
        if len(s) >= 2 and rdict[s[0]] < rdict[s[1]]:
            t += rdict[s[1]] - rdict[s[0]]
            s = s[2:]
        else:
            t += rdict[s[0]]
            s = s[1:]
    return t

##for s in nums:
##    print s, RN(s), NR(RN(s))

numsa = [NR(RN(s)) for s in nums]
print sum(len(s) for s in nums)-sum(len(s) for s in numsa)
    
