from datetime import datetime
from math import *

def divsum(x):
    #divs = []
    s = 0
    for n in range(1,(x/2)+1):
        if x%n == 0:
            #divs.append(n)
            s += n
    #return sum(divs)
    return s

def divSum(x):
    return sum(n for n in xrange(1,x/2+1) if not x%n)

def Divsum(x):
    s = 1
    for n in range(2,int(x**0.5)+1):
        if not x%n: s += n+x/n
    if (x**0.5).is_integer(): s -= x**0.5
    return s

##abund = []
##
##for n in range(20200):
##    if n < divsum(n):
##        abund.append(n)
##
##print 'abund complete at '+str(len(abund))
##
##abundsums = []
##
##for n in range(len(abund)):
##    for m in range(len(abund[n:-1])):
##        nn = abund[n]
##        mm = abund[m]
##        if nn+mm > 20200: break
##        if nn+mm not in abundsums:
##            abundsums.append(nn+mm)
##            print nn, mm, nn+mm
##
##nums = []
##
##for n in range(20200):
##    if n not in abundsums:
##        nums.append(n)
##        print n
##    
##print sum(nums)

abund = []
nonabund = set([])
abundsum = set([])

start = datetime.now()
for n in range(1,20200):
    nonabund.add(n)
    if Divsum(n) > n:
        abund.append(n)
for a in abund:
    for b in abund:
        abundsum.add(a+b)
print sum(nonabund - abundsum)
print datetime.now() - start

abundants = set(i for i in range(1,20200) if Divsum(i) > i)

def abundantsum(i):
    return any(i-a in abundants for a in abundants)
print sum(i for i in range(1,20200) if not abundantsum(i))
