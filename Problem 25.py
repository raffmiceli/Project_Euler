#print 1,1
#print 2,1

a = 1
b = 1
c = 0
n = 2

while len(str(c)) != 1000:
    c = a + b
    a = b
    b = c
    #print n,c
    n += 1
#print n,c
print n

f=[1,1]
while len(str(f[-1]))<1000:
    f.append(f[-1]+f[-2])
print len(f)

def fiblen(n):
    a,b,n = 1,1,2
    while len(str(b)) != 1000:
        a,b,n = b,a+b,n+1
    return n

print fiblen(1000)


