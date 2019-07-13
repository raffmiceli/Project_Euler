def memoize(f):
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x] = f(*x)
        return memf.cache[x]
    memf.cache = {}
    return memf

def memoize(f):
    cache = {}
    def memf(*x):
        if x not in cache:
            cache[x] = f(*x)
        return cache[x]
    return memf
