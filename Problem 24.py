from math import *

def megaperm(m):
    digits1 = ['0','1','2','3','4','5','6','7','8','9']
    n = 1
    for a in digits1:
        digits2 = digits1[:]
        digits2.remove(a)
        for b in digits2:
            digits3 = digits2[:]
            digits3.remove(b)
            for c in digits3:
                digits4 = digits3[:]
                digits4.remove(c)
                for d in digits4:
                    digits5 = digits4[:]
                    digits5.remove(d)
                    for e in digits5:
                        digits6 = digits5[:]
                        digits6.remove(e)
                        for f in digits6:
                            digits7 = digits6[:]
                            digits7.remove(f)
                            for g in digits7:
                                digits8 = digits7[:]
                                digits8.remove(g)
                                for h in digits8:
                                    digits9 = digits8[:]
                                    digits9.remove(h)
                                    for i in digits9:
                                        digits10 = digits9[:]
                                        digits10.remove(i)
                                        for j in digits10:
                                            #print n
                                            if n == m:
                                                return a+b+c+d+e+f+g+h+i+j
                                            n += 1
#print megaperm(1000000)

def fact(n):
    if n == 0: return 1
    else: return n*fact(n-1)

def findperm(n):
    dig = range(10)
    find = n
    ans = ''
    num = 10

    while len(dig) != 1:
        num -= 1
        a = factorial(num)
        b = int(ceil(find/float(a)))
        this = dig[b-1]
        ans = ans+str(this)
        dig.remove(this)
        find = find - a*(b-1)
    else: ans = ans+str(dig[0])
    return ans
#print findperm(1000000)

nums=[0,1,2,3,4,5,6,7,8,9]

def perm(n,l):
    f=factorial(l)
    return divmod(n,f)

def n_perm(d, n):
    n-=1
    l=len(d)-1
    s=''
    while l>=0:
        q,n=perm(n,l)
        s+=str(d.pop(q))
        l-=1
    return s
#print n_perm(nums,1000000)

def factoradic(n):
    if not n: return '0'
    fr = ''
    a = 1
    while factorial(a+1) <= n: a+=1
    for m in range(a,-1,-1):
        fm = factorial(m)
        d = n/fm
        n = n%fm
        fr += str(d)
    return fr

def facperm(n,l):
    ans = ''
    digs = range(l)
    for a in factoradic(n-1):
        ans += str(digs.pop(int(a)))
    return ans

#print facperm(1000000,10)

def facPerm(n,l):
    ans = ''
    digs = range(l)
    a = len(digs)-1
    n -= 1
    for m in range(a,-1,-1):
        fm = factorial(m)
        d = n/fm
        n = n%fm
        ans += str(digs.pop(d))
    return ans

print facPerm(1000000,10)
