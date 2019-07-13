def lychCount(x):
    lych = 0
    for n in range(1,x+1):
        for m in range(50):
            n += int(str(n)[::-1])
            if str(n) == str(n)[::-1]: break
        else: lych += 1
    return lych

print lychCount(10000)

def lychList(x):
    lyches = []
    for n in range(1,x+1):
        keep = n
        for m in range(50):
            n += int(str(n)[::-1])
            if str(n) == str(n)[::-1]: break
        else: lyches.append(keep)
    return lyches

#print lychList(10000)

def revTime(x):
    time = 0
    while True:
        time += 1
        x += int(str(x)[::-1])
        if str(x) == str(x)[::-1]: break
    return time

#print revTime(196)
