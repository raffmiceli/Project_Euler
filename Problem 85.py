from operator import mul

def tri(n):
    return n*(n+1)/2

def NumRects(a,b):
    return tri(a)*tri(b)

def Numrects(a,b):
    return a*(a+1)*b*(b+1)/4

def numrects(a,b):
    rects = 0
    for x in range(1,a+1):
        for y in range(1,b+1):
            new = (a-x+1)*(b-y+1)
            rects += new
    return rects

lim = 2000000
pairs,sols,difs = [],[],[]
for a in range(1,100):
    for b in range(a,100):
        pairs.append((a,b))
        r = numrects(a,b)
        sols.append(r)
        difs.append(abs(lim-r))
        if r > lim: break
mi = min(difs)
mii = difs.index(min(difs))
winner = pairs[mii]
print sols[mii],winner,reduce(mul,winner)
