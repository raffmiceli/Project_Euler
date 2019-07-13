import string, itertools
code = eval(open('cipher1.txt').read())

def best_match(code):
    good_chars=set(map(ord, string.ascii_letters) + [ord(" ")])
    maxscore=0
    bestletter=None
    for letter in map(ord,string.lowercase):
        score = 0
        for c in code:
            if (c ^ letter) in good_chars:
                score += 1
        if score > maxscore:
            maxscore   = score
            bestletter = letter
    return bestletter

pad = [best_match(code[::3]), best_match(code[1::3]), best_match(code[2::3])]

print sum((ch ^ p) for (ch,p) in zip(code, itertools.cycle(pad)))
decode = ''
for n in range(len(code)):
    decode += chr(code[n]^pad[n%3])
print decode
