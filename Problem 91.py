tris = 0
for x1 in xrange(51):
    for y1 in xrange(51):
        for x2 in xrange(51):
            for y2 in xrange(51):
##                if y2-x2 > y1-x1: continue
##                if (x1 == x2 == 0) or \
##                   (y1 == y2 == 0): continue
                a = x1**2+y1**2
                b = x2**2+y2**2
                c = (x1-x2)**2+(y1-y2)**2
                if min(a,b,c) == 0: continue
                if a+b == c or a+c == b or \
                   b+c == a: tris += 1
print tris/2
#print tris

def gcd(x, y): return gcd(y,x%y) if y else x

def problem091(n):
    count = 0
    for x in xrange(1, n+1):
        for y in xrange(1, x):
            a, b = x/gcd(x, y), y/gcd(x, y)
            count += min((n-x)/b, y/a) + min(x/b, (n-y)/a)
    return 2*count + (7*n**2)/2

def countTr(N):
   res = 0
   for x1 in range(0,N+1):
      for x2 in range(x1+1,N+1):
         xx = x1 * (x2 - x1)
         for y1 in range(1, N+1):
            y2 = y1 - xx/y1
            if y2 >= 0 and xx % y1 == 0:
               res += 1
   return res * 2 + N**2
   
print countTr(50)

def main(a):
    total=a**2*3
    for x in range(1,a+1):
        for y in range(1,x+1):
            if x==y:
                total+=min(x,(a-x))*2
            else:
                g=gcd(x,y)
                my=y/g
                mx=x/g
                total+=min(y/mx,(a-x)/my)*2
                total+=min(x/my,(a-y)/mx)*2
    print total
main(50)
                
