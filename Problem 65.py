from time import *

start = time()
a = [0,0,2]
for n in xrange(1,34):
    a += [1,2*n,1]
#print a

p = [0,1,2]
#q = [1,0,1]

for n in xrange(3,102):
    p.append(a[n]*p[n-1]+p[n-2])
    #q.append(a[n]*q[n-1]+q[n-2])

#print p[101], sum(int(c) for c in str(p[101]))
print sum(map(int,str(p[101])))
print time()-start

##t1 = clock()
##seq = [2]
##for k in xrange(1,34):
##    seq += [1,2*k,1]
##
##num = den = 1
##
##for i in seq[:99][::-1]:
##    i *= den
##    num += i
##    num,den = den,num
##
##total = sum(int(i) for i in str(den))
##
##print total
##print clock()-t1

##def PE065(N=100):
##  p=2
##  P=2*1+1
##  for n in range(2, N):
##    if n%3==2:
##      p, P = P, P*2*(n//3+1)+p
##    else:
##      p, P = P, P+p
##  return sum(int(c) for c in str(P))
##
##
##def PE065(N=100):
##  k=N//3
##  #p=1
##  #P=2
##  p=1
##  P=2
##  for n in range(2, 2*k+2, 2):
##      pP = p+P
##      nPp = n*pP + P
##      P = nPp+pP
##      p = nPp
##      #P, p = (n+2)*P+(n+1)*p, (n+1)*P+n*p
##  Pstr=str(P)
##  return sum(ord(c) for c in Pstr)-48*len(Pstr)
