def rankHand(cards):
    values = sorted(['23456789TJQKA'.find(c[0]) for c in cards])
    isStraight = False not in [values[i] == values[0]+i for i in xrange(0, 5)]
    isFlush = False not in [c[1] == cards[0][1] for c in cards]
    vc = {}
    for v in values:
        vc[v] = values.count(v)
    combos = sorted([(b, a) for a, b in vc.items()])
    kinds = [c[0] for c in reversed(combos)]
    kvalues = [c[1] for c in reversed(combos)]
    if isStraight and isFlush and values[0] == 8:
        return ['J:royal flush'] + kvalues
    if isStraight and isFlush:
        return ['I:straight flush'] + kvalues
    if kinds[0] == 4:
        return ['H:four kind'] + kvalues
    if kinds[0] == 3 and kinds[1] == 2:
        return ['G:full house'] + kvalues
    if isFlush:
        return ['F:flush'] + kvalues
    if isStraight:
        return ['E:straight'] + kvalues
    if kinds[0] == 3:
        return ['D:three kind'] + kvalues
    if kinds[0] == 2 and kinds[1] == 2:
        return ['C:two pair'] + kvalues
    if kinds[0] == 2:
        return ['B:pair'] + kvalues
    return ['A:high'] + kvalues

total = 0
for l in open('poker.txt'):
    cards = l.split()
    h1 = rankHand(cards[:5])    
    h2 = rankHand(cards[5:])
    if h1 > h2:
        total = total + 1
print total
