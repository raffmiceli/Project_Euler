from string import *
from time import *

def XOR(cod,key):
    res = ''
    for n in range(8):
        if (int(cod[n]) and not int(key[n])) or (not int(cod[n]) and int(key[n])):
            res += '1'
        else: res += '0'
    return res

def decode(text,key):
    num = len(text)/len(key)+1
    decoder = num*key
    decoded = ''
    for n in xrange(len(text)):
        c = chr(int(XOR(text[n],bin(ord(decoder[n]))[2:].zfill(8)),2))
        decoded += c
    return decoded

f = open('cipher1.txt','r')
g = f.read()
f.close()
chars = g.split(',')
chars[-1] = '73'
lower = ascii_lowercase
valid = ascii_uppercase+ascii_lowercase+" ,.?!':;()"+'"'+'0123456789'
#valid = ascii_uppercase+ascii_lowercase+" ,.?!':;()0123456789"
keys = [a+b+c for a in lower for b in lower for c in lower]
bins = [bin(int(c))[2:].zfill(8) for c in chars]
num = len(chars)/3+1
vowels = 'aeiou'

best = 1200
bestkey = ''
start = time()
for key in keys:
    #if key[1:] == 'aa': print key
    if all(c not in vowels for c in key): continue
    decoder = num*key
    decoded = ''
    nonval = 0
    for n in xrange(len(bins)):
        c = chr(int(XOR(bins[n],bin(ord(decoder[n]))[2:].zfill(8)),2))
        decoded += c
        if c not in valid:
            nonval += 1
        if nonval > best: break
    if nonval < best:
        best = nonval
        bestkey = key
        print key, nonval
    if best == 0: break
print bestkey, best

decoded = decode(bins,bestkey)
print decoded, sum(ord(c) for c in decoded)
print time()-start
