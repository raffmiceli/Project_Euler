f = open('names.txt','r')
g = '",'+f.read()+',"'
names = sorted(g.split('","')[1:-1])
f.close()

total = 0
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def wordscore(word):
    alph = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', xrange(1,27)))
    return sum(alph[l] for l in word)

def wordScore(word):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return sum(letters.find(l)+1 for l in word)
        

for n in range(len(names)):
##    t = 0
##    for l in names[n]:
##        t += letters.find(l)+1
##    total += t*(n+1)
    total += wordScore(names[n])*(n+1)
print total

names = open('names.txt').read().replace('"','').split(",")
print sum(wordScore(word)*n for n,word in enumerate(sorted(names),1))




