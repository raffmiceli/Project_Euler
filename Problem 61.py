from time import *

def tri(n): return n*(n+1)/2
def squ(n): return n**2
def penta(n): return n*(3*n-1)/2
def hexa(n): return n*(2*n-1)
def hepta(n): return n*(5*n-3)/2
def octa(n): return n*(3*n-2)
def blist(nums,n): return [m for m in nums if str(n)[2:] == str(m)[:2]]
def elist(nums,n): return [m for m in nums if str(n)[:2] == str(m)[2:]]

tris = [tri(n) for n in xrange(40,150,2) if len(str(tri(n))) == 4]
squs = [squ(n) for n in xrange(30,100) if len(str(squ(n))) == 4]
pentas = [penta(n) for n in xrange(20,90) if len(str(penta(n))) == 4]
hexas = [hexa(n) for n in xrange(20,80) if len(str(hexa(n))) == 4]
heptas = [hepta(n) for n in xrange(20,70) if len(str(hepta(n))) == 4]
octas = [octa(n) for n in xrange(10,60) if len(str(octa(n))) == 4]

fnums = sorted(set(tris+squs+pentas+hexas+heptas+octas))
valids = [v for v in fnums if blist(fnums,v) and elist(fnums,v)]
flists = [tris,squs,pentas,hexas,heptas,octas]
blists = {n:blist(valids,n) for n in valids}

def cfn():
    for a in valids:
        for b in blists[a]:
            for c in blists[b]:
                for d in blists[c]:
                    for e in blists[d]:
                        for f in blists[e]:
                            if str(a)[:2] == str(f)[2:]:
                                sol = [a,b,c,d,e,f]
                                table = [[n in fl for n in sol] for fl in flists]
                                if all(r.count(True) == 1 for r in table):
                                    print sol, sum(sol); return
start = time()
cfn()
print time()-start

##def tlist(nums,n):
##    trues = []
##    sn = str(n)
##    for m in nums:
##        if n == m: continue
##        sm = str(m)
##        if sn[2:] == sm[:2]:
##            trues.append(m)
##    return trues

##A = [[] for i in range(9)]
##for i in xrange(3,9):
##    for n in xrange(10000):
##        p = n * ((i-2) * n - (i - 4))/2
##        if p >= 10000: break
##        if p >= 1000: A[i].append(p)
##def dfs(X,A):
##    if len(X) == 6:
##        if X[-1] % 100 == X[0] / 100:
##            print sum(X)
##            print X
##            exit()
##    for a in A:
##        for x in a:
##            if len(X) == 0 or X[-1] % 100 == x / 100:
##                dfs(X+[x],[b for b in A if b != a]) 
##dfs([],A)

##from collections import defaultdict
##import operator
##
##c = ( (1,1,2), (1,0,1), (3,-1,2), (2,-1,1), (5,-3,2), (3,-2,1) )
##p = [ [ x for x in [ n*(c[r][0]*n+c[r][1])/c[r][2] for n in xrange(142) ] if x>999 and x<=9999 ] for r in xrange(6) ]
##pd = [ reduce(lambda x, (k,v): x[k].append(v) or x, zip(map(lambda n:str(n)[:2],p[i]),map(str,p[i])), defaultdict(list)) for i in xrange(6) ]
##
##def findcycle(nset, chain):
##    if len(nset) == 0 and chain[0][1][:2] == chain[-1][1][2:]: 
##        print chain, sum(map(lambda x:int(x[1]), chain)); return
##    candidates = [[(i,x) for x in pd[i][chain[-1][1][2:]]] for i in nset]
##    if len(candidates) == 0: return
##    for c in reduce(operator.add, candidates): 
##        findcycle(nset-set([c[0]]), chain+[c])
##        
##for n in map(lambda n:str(n), p[5]): 
##    findcycle(set(xrange(5)), [(5,n)])

