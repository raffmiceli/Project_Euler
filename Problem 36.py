def revStr(aStr):
    if len(aStr) <= 1: return aStr
    return aStr[-1]+revStr(aStr[1:-1])+aStr[0]

def isPal(n):
    return str(n) == str(n)[::-1]

def bincon(x):
    if x == 0: return '0'
    if x < 0:
        isNeg = True
        x = abs(x)
    else: isNeg = False
    result = ''
    while x > 0:
        result = str(x%2) + result
        x = x/2
    if isNeg: result = '-' + result
    return result

def binc(n):
    s = ''
    while n > 0:
        s = str(n%2)+s
        n = n >> 1
    return s

def DBPalSum1(x):
    true = []
    for n in xrange(1,x,2):
        if str(n) == revStr(str(n)):
            if bincon(n) == revStr(bincon(n)):
                true.append(n)
                #print n, bincon(n)
    return sum(true)

def DBPalSum2(x):
    s = 0
    for n in xrange(1,x,2):
        if isPal(n) and isPal(binc(n)):
            s += n
            #print n
    return s

def DBPalSum3(x):
    return sum(n for n in xrange(1,x,2) if isPal(n) and isPal(binc(n)))
