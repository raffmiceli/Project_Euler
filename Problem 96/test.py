from time import time
from copy import copy
'''
math_96 - Sudoku Puzzles
'''
space=-1
def rep(st,p,s):
   return st[:p]+s+st[p+1:]
def p_p(P):
    # Print puzzle
    for a in range(9):
        if not a%3: print ''
        print ' '*space,
        for b in range(9):
            if not b%3: print '|',
            print P[a][b],
        print '|'
def cube_xy(a,b):
    # 0-8
    return [a/3*3,b/3*3]
def is_good(P,a,b,n):
    # 0-8
    # check current cube:
    c=cube_xy(a,b)
    for x in range(c[0],c[0]+3):
        for y in range(c[1],c[1]+3):
            if int(P[x][y]) == n and (x!=a or y!=b): return False
    y=b
    for x in range(9):
        if int(P[x][y]) == n and x!=a: return False
    x=a
    for y in range(9):
        if int(P[x][y]) == n and y!=b: return False
    return True
def good(P,a,b):
    # 0-8
    # returns list of good numbers
    ret=[]
    for n in range(1,10):
        if is_good(P,a,b,n):
            ret.append(n)
    return ret
def zero(P):
    # checks if there are any zeroes left
    #p_p(P)
    for a in range(9):
        for b in range(9):
            if P[a][b]=='0': return True
    return False # -> no zeroes.

def sud_1(P):
    flag = 0
    # Simple logic check -> check if x,y can only have one value.
    for a in range(9):
        for b in range(9):
            if P[a][b]!='0': continue
            t=good(P,a,b)
            if len(t)==1:
                t=str(t[0])
                P[a]=rep(P[a],b,str(t))
                flag = 1
    if flag:
        return sud_1(P)
    else:
        return P

def solve(P):
    global space
    space+=1
    P_=copy(P)
    P=sud_1(P)
    if not zero(P):
        space-=1
        return P
    for a in xrange(9):
        for b in xrange(9):
            if P[a][b]=='0':
                if (len(good(P,a,b)) == 0):
                    #print ' '*space+'Return:', P[0], P_[0], 'bad'
                    space-=1
                    return P_
                for n in good(P,a,b):
                    #print ' '*space+'Trying..', str(a+1)+','+str(b+1), '->', n, good(P,a,b)
                    P[a]=rep(P[a],b,str(n))
                    P=solve(P)
                    if not zero(P):
                        #print ' '*space+'Return:', P[a], P_[a], 'done.'
                        space-=1
                        return P
                    #print ' '*space+'Bad:', P[a], '->>', P_[a]
                    P=copy(P_)
                #print ' '*space+'Return:', P[a], P_[a], 'bad'
                space-=1
                return P_
ti = time()

f=file("sudoku.txt")
#f.open()
i=0
st=1
P=[]
su=0
x=0
while st:
    st=f.readline()
    if i!=0:
        P.append(st)
    if i==9:
        x+=1
        print '---------------', time()-ti, 's', x
        p_p(P)
        P=solve(P)
        su+=int(P[0][:3])
        p_p(P)
        P=[]
        i=-1
    i+=1
'''
p_p(P)
print '--------------->'
P=solve(P)

p_p(P)
'''
print su, time()-ti, 's'
