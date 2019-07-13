from datetime import datetime

def coins200():
    coins = [1,2,5,10,20,50,100,200]
    true = 8
    steps = 200*100*40*20*10*4*2
    p = steps/100
    s = 0
    for a in range(200):
        if a*1 > 200: break
        for b in range(100):
            if a*1+b*2 > 200: break
            for c in range(40):
                if a*1+b*2+c*5 > 200: break
                for d in range(20):
                    if a*1+b*2+c*5+d*10 > 200: break
                    for e in range(10):
                        if a*1+b*2+c*5+d*10+e*20 > 200: break
                        for f in range(4):
                            if a*1+b*2+c*5+d*10+e*20+f*50 > 200: break
                            for g in range(2):
                                s += 1
                                t = a*1+b*2+c*5+d*10+e*20+f*50+g*100
                                if t == 200:
                                    true += 1
                                    #print s, true
    return true

##start = datetime.now()
##print coins200()
##print datetime.now()-start

def coinSums(coins,val):
    if len(coins) == 1: return val%coins[0] and 0 or 1
    return sum(coinSums(coins[1:],newVal) for newVal in xrange(val,-1,-coins[0]))

#print coinSums([200,100,50,20,10,5,2,1],500)

#thfourtheye solution
def tfecoins(Target):
    Coins  = [1, 2, 5, 10, 20, 50, 100, 200]
    Previous = [0]*(Target+1)
    Current  = [0]*(Target+1)

    for coin in Coins:
        Current[0] = 1
        for denom in range(1, Target+1):
            if denom < coin: Current[denom] = Previous[denom]
            else: Current[denom] = Current[denom - coin] + Previous[denom]
        Previous = Current
    return Current[Target]

#print tfecoins(100000)

#rassefrasse solution

def rfcoins(n):
    purse = [2, 5, 10, 20, 50, 100, 200]
    sums = [1]*(n+1)
    for coin in purse:
        for x in range(coin,n+1):
            sums[x] += sums[x-coin]
    return sums[n]

#print rfcoins(100000)


def newCoinLoop(t):
    ways = 0
    for a in xrange(t,-1,-200):
        for b in xrange(a,-1,-100):
            for c in xrange(b,-1,-50):
                for d in xrange(c,-1,-20):
                    for e in xrange(d,-1,-10):
                        for f in xrange(e,-1,-5):
                            for g in xrange(f,-1,-2):
                                ways += 1
    return ways

print newCoinLoop(200)

def dpcoins(n):
    target = n
    coinSizes = [1,2,5,10,20,50,100,200]
    ways = [0]*(target+1)
    ways[0] = 1
    for i in xrange(len(coinSizes)):
        for j in xrange(coinSizes[i],target+1):
            ways[j] += ways[j - coinSizes[i]]
    return ways[n]

print dpcoins(200)
