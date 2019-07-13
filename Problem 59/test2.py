import itertools

keyrange = [ord('a') + i for i in range(27)]
crypt = [int(c) for c in open("cipher1.txt").readline()[:-1].split(',')]

for key in itertools.product(keyrange, keyrange, keyrange):
    text = ''.join([chr(crypt[i] ^ key[i % len(key)]) for i in range(len(crypt))])
    if "world" in text:
        print(sum(ord(text[i]) for i in range(len(text))))
        break
