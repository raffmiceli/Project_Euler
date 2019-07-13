##board = ['GO','A1','CC1','A2','T1','R1','B1','CH1','B2','B3',\
##          'JAIL','C1','U1','C2','C3','R2','D1','CC2','D2','D3',\
##          'FP','E1','CH2','E2','E3','R3','F1','F2','U2','F3',\
##          'G2J','G1','G2','CC3','G3','R4','CH3','H1','T2','H2']

from random import *

sdict = {n:0 for n in range(40)}
CC = range(16); shuffle(CC)
CH = range(16); shuffle(CH)
CCi,CHi = [2,17,33],[7,22,36]
CHc = [0,10,11,24,31,5]
Rs,Us = [5,15,25,35],[12,28]
cur = 0
si = 4
rolls = []
turns = 10**6
for n in xrange(turns):
    roll = (randrange(si)+1,randrange(si)+1)
    rolls.append(roll)
    if len(rolls) >= 3:
        if all(r[0] == r[1] for r in \
               [rolls[-1],rolls[-2],rolls[-3]]):
            cur = 10
        else: cur = (cur+sum(roll))%40
    else: cur = (cur+sum(roll))%40
    if cur in CCi:
        card = CC[-1]
        if card == 0: cur = 0
        if card == 1: cur = 10
        CC = [card]+CC[:-1]
    if cur in CHi:
        card = CH[-1]
        if card < 6: cur = CHc[card]
        if card in [6,7]:
            while cur not in Rs:
                cur = (cur + 1)%40
        if card == 8:
            while cur not in Us:
                cur = (cur + 1)%40
        if card == 9: cur -= 3
        CH = [card]+CH[:-1]
    if cur == 30: cur = 10
    sdict[cur] += 1
vals = sorted(sdict.values())
f,s,t = vals[-1],vals[-2],vals[-3]
for n in range(40):
    if sdict[n] == f: fn = n
    if sdict[n] == s: sn = n
    if sdict[n] == t: tn = n
print f,s,t
print fn,sn,tn
