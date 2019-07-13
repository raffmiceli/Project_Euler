def P086(target=1000000):
    
    def ptriplets(a=3, b=4, c=5):
        sol = [(x,y) for x,y in ((a,b),(b,a)) if x<=limit and y<2*x]
        if not sol: 
            return
        for a,b in sol:
            primitives.append((a,b))
        ptriplets(a-2*b+2*c, 2*a-b+2*c, 2*a-2*b+3*c)
        ptriplets(a+2*b+2*c, 2*a+b+2*c, 2*a+2*b+3*c)
        ptriplets(-a+2*b+2*c, -2*a+b+2*c, -2*a+2*b+3*c)
    
    limit = int(target**0.5)*2
    counts = [0]*(limit+1)
    primitives = []
    ptriplets()
    for a, b in primitives:
        for i in xrange(1,limit/a+1): 
            na, nb = a*i,b*i
            counts[na] += nb/2
            if nb>na+1: counts[na] += na+1-nb
            
    subtotal=0
    for i,x in enumerate(counts):
        subtotal+=x
        if subtotal > target:
            return i
print P086()
