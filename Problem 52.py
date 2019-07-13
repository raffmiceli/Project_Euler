for n in range(100000,200000):
    check = sorted(str(n))
    mul = [a*n for a in range(1,7)]
    areperms = [sorted(str(m)) == check for m in mul]
    if all(areperms): print mul; break
