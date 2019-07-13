# 1 - Royal Flush
# 2 - Straight Flush
# 3 - Four of a Kind
# 4 - Full House
# 5 - Flush
# 6 - Straight
# 7 - Three of a Kind
# 8 - Two Pairs
# 9 - One Pair
#10 - High Card

f = open('poker.txt','r')
hands = f.readlines()
f.close()

P1w = 0
P2w = 0

def Rank(hand):
    valsdict = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'J':10,'Q':11,'K':12,'A':13}
    royal = sorted(['T','J','K','Q','A'])
    vals = [c[0] for c in hand]
    suits = [c[1] for c in hand]
    sortedvals = sorted([valsdict[a] for a in vals])
    setvals = set(vals)
    counts = sorted([vals.count(a) for a in setvals])
    low = sortedvals[0]
    high = sortedvals[-1]
    numsuits = len(set(suits))
    numvals = len(set(vals))
    isflush = numsuits == 1
    isroyal = isflush and sorted(vals) == royal
    isstraight = sortedvals == range(low,low+5)
    if isroyal: return 1
    if isflush:
        if isstraight: return 2
        else: return 5
    if isstraight: return 6
    if numvals == 4: return 9
    if numvals == 2:
        if counts == [2,3]: return 4
        if counts == [1,4]: return 3
    if numvals == 3:
        if counts == [1,2,2]: return 8
        if 3 in counts: return 7
    return 10

def High(hand):
    valsdict = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'J':10,'Q':11,'K':12,'A':13}
    vals = [c[0] for c in hand]
    sortedvals = sorted([valsdict[a] for a in vals])
    setvals = set(vals)
    high = sortedvals[-1]
    R = Rank(hand)
    meh = [1,2,5,6,10]
    if R in meh: return high
    if R == 3:
        for a in setvals:
            if vals.count(a) == 4:
                return valsdict[a]
    if R == 4 or R == 7:
        for a in setvals:
            if vals.count(a) == 3:
                return valsdict[a]
    if R == 9:
        for a in setvals:
            if vals.count(a) == 2:
                return valsdict[a]
    if R == 8:
        highs = []
        for a in setvals:
            if vals.count(a) == 2:
                highs.append(valsdict[a])
        return max(highs)

for hand in hands:
    hand = hand.split()
    P1 = hand[:5]
    P2 = hand[5:]
    P2[4] = P2[4][:2]
    P1r = Rank(P1)
    P2r = Rank(P2)
    P1h = High(P1)
    P2h = High(P2)
    if P1r == P2r:
        if P1h > P2h: P1w += 1
        else: P2w += 1
    elif P1r < P2r: P1w += 1
    else: P2w += 1
    #print P1,P2,P1r,P2r,P1h,P2h,P1w,P2w
print P1w, P2w

##def HighRank(hand):
##    valsdict = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'J':10,'Q':11,'K':12,'A':13}
##    royal = sorted(['T','J','K','Q','A'])
##    vals = [c[0] for c in hand]
##    suits = [c[1] for c in hand]
##    sortedvals = sorted([valsdict[a] for a in vals])
##    setvals = set(vals)
##    counts = sorted([vals.count(a) for a in setvals])
##    low = sortedvals[0]
##    high = sortedvals[-1]
##    numsuits = len(set(suits))
##    numvals = len(set(vals))
##    isflush = numsuits == 1
##    isroyal = isflush and sorted(vals) == royal
##    isstraight = sortedvals == range(low,low+5)
##    if isroyal: return [1,high]
##    if isflush:
##        if isstraight: return [2,high]
##        else: return [5,high]
##    if isstraight: return [6,high]
##    if numvals == 4:
##        for a in setvals:
##            if vals.count(a) == 2:
##                return [9,valsdict[a]]
##    if numvals == 2:
##        if counts == [2,3]:
##            for a in setvals:
##                if vals.count(a) == 3:
##                    return [4,valsdict[a]]
##        if counts == [1,4]:
##            for a in setvals:
##                if vals.count(a) == 4:
##                    return [3,valsdict[a]]
##    if numvals == 3:
##        if counts == [1,2,2]:
##            highs = []
##            for a in setvals:
##                if vals.count(a) == 2:
##                    highs.append(valsdict[a])
##            return [8,max(highs)]
##        if 3 in counts:
##            for a in setvals:
##                if vals.count(a) == 3:
##                    return [7,valsdict[a]]
##    return [10,high]
##
##for hand in hands:
##    hand = hand.split()
##    P1 = hand[:5]
##    P2 = hand[5:]
##    P2[4] = P2[4][:2]
##    P1r,P1h = HighRank(P1)[0],HighRank(P1)[1]
##    P2r,P2h = HighRank(P2)[0],HighRank(P2)[1]
##    if P1r == P2r:
##        if P1h > P2h: P1w += 1
##        else: P2w += 1
##    elif P1r < P2r: P1w += 1
##    else: P2w += 1
##    #print P1,P2,P1r,P2r,P1h,P2h,P1w,P2w
##print P1w, P2w
