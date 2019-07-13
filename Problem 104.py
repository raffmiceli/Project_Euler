from math import *

a,b = 1,1
k = 3
check = [str(n) for n in range(1,10)]

##n = 1
##x,y = 0,1
phi = (sqrt(5)+1)/2.0
##aa,bb = 1,1
##head = 10**15
##tail = 10**9
##
##while True:
##    a,b = b,a+b
##    aa,bb = bb,aa+bb
##    a %= tail
##    b %= tail
##    if aa > head and bb > head:
##        aa /= 10
##        bb /= 10
##    if sorted(str(b)) == check:
##        if sorted(str(bb)[:9]) == check:
##            break
##    k += 1
##print k


##while len(str(a)) < 18:
##    a,b = b,a+b
##    k += 1
##
##ast,aen = int(str(a)[:15]),int(str(a)[-9:])
##bst,ben = int(str(b)[:15]),int(str(b)[-9:])
##
##while True:
##    if not k%1000: print k, ast, bst
##    ast,bst = bst, int(str(ast+bst)[:15])
##    aen,ben = ben, int(str(aen+ben)[-9:])
##    if sorted(str(ben)) == check and\
##       sorted(str(bst)[:9]) == check:
##        break
##    k += 1
##print k

while True:
    a,b = b,int(str(a+b)[-9:])
    if sorted(str(b)) == check:
        t = (k)*log(phi,10)-log(sqrt(5),10)
        t -= int(t)
        st = str(int(round(10**(t+8))))
        if sorted(st) == check: break
    k += 1
print k

##while n <= 100:
##    print int(round((phi**n)/sqrt(5))),y
##    x,y = y,x+y
##    n += 1

##while True:
##    if not k%1000: print k, len(str(b))
##    a,b = b,a+b
##    if sorted(str(b)[:9]) == check:
##        if sorted(str(b)[-9:]) == check:
##            break
##    k += 1
##print k

##while len(str(a)) < 18 and len(str(b)) < 18:
##    a,b = b,a+b
##    k += 1
##
##ast,aen = int(str(a)[:9]),int(str(a)[9:])
##bst,ben = int(str(b)[:9]),int(str(b)[9:])
##
##while True:
##    if not k%1000: print k
##    ast,bst = bst,(int(str(ast+bst)[:9]))
##    aen,ben = ben,(int(str(aen+ben)[-9:]))
##    if sorted(str(bst)) == check and\
##       sorted(str(ben)) == check: break
##    k += 1
##print k
