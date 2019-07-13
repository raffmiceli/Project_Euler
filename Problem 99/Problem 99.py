from math import *
best,bestl,n = 0,0,1
for line in open('base_exp.txt'):
    l = line.split(',')
    a,b = int(l[0]),int(l[1])
##    l = eval(line)
##    a,b = l[0],l[1]
    num = b*log(a)
    if num > best:
        best,bestl = num,n
    n += 1
print bestl
    
