from string import *
from time import *

def decode(text,key):
    decoded = ''
    for n in xrange(len(text)):
        c = chr(ints[n]^ord(key[n%3]))
        decoded += c
    return decoded

f = open('cipher1.txt','r')
chars = f.read().split(',')
f.close()
valid = set(printable)-set("#$%&*+-<=>^[]\\_{}|~")
l = ascii_lowercase
keys = [a+b+c for a in l for b in l for c in l]
ints = [int(c) for c in chars]
vowels = 'aeiou'

best = 1201
bestkey = ''
start = time()
for key in keys:
    if all(c not in vowels for c in key): continue
    decoded = ''
    nonval = 0
    for n in xrange(len(ints)):
        c = chr(ints[n]^ord(key[n%3]))
        decoded += c
        if c not in valid:
            nonval += 1
        if nonval > best: break
    if nonval < best:
        best = nonval
        bestkey = key
        #print key, nonval
    if best == 0: break
#print bestkey, best

decoded = decode(ints,bestkey)
print decoded, sum(ord(c) for c in decoded), time()-start
