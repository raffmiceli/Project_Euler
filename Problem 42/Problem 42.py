f = open('words.txt','r')
g = f.read()
f.close()
words = g.split('","')

def tri(n):
    return n*(n+1)/2

def lsum(word):
    t = 0
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for c in word:
        t += letters.find(c)+1
    return t

tris = []
for n in xrange(1,21):
    tris.append(tri(n))

total = 0
for word in words:
    if lsum(word) in tris:
        total += 1
print total

def lSum(w):
    return sum(ord(c)-64 for c in w)

tris = [tri(n) for n in xrange(1,21)]

print sum([1 for w in words if lsum(w) in tris])
    
