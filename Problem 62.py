##cubes = [n**3 for n in xrange(10000)]
##pos = []
##for c in cubes:
##    s = ''.join(sorted(str(c)))
##    if s not in pos:
##        pos.append(s)
##
##posdict = {n:[] for n in pos}
##
##for c in cubes:
##    s = ''.join(sorted(str(c)))
##    posdict[s].append(c)
##
##for k in posdict.keys():
##    if len(posdict[k]) == 5:
##        print k, posdict[k]

jss = lambda x: ''.join(sorted(str(x)))
cubes = [n**3 for n in xrange(10000)]
strings = map(jss,cubes)
for c in cubes:
    if strings.count(jss(c)) == 5:
        print c; break

##cubes = {}
##for i in xrange(1, 10000):
##    key=''.join(sorted(str(i**3)))
##    if not cubes.has_key(key): cubes[key] = []
##    cubes[key].append(i**3)
##print min([min(c) for c in cubes.values() if len(c)==5])

##cubes = [sorted(str(x**3)) for x in range(10000)]
##counts = [cubes.count(x) for x in cubes]
##print counts.index(5)**3

##cubes = {}
##i = 0
##while True:
##    i += 1
##    n = i ** 3
##    s = "".join(sorted(list(str(n))))
##    val = cubes.setdefault(s, [0, []])[0] + 1
##    cubes[s][0] = val
##    cubes[s][1].append(n)
##    if val == 5:
##        print min(cubes[s][1])
##        break

##p,v,i = 5,{},1
##while True:
##    key = ''.join(sorted(str(i**3)))
##    try: v[key].append(i)
##    except: v[key] = [i] 
##    if len(v[key]) == p:
##        print min(v[key])**3; break
##    i += 1

##def problem62():
##    d = {}
##    for x in xrange(1000,10000):
##        z = ''.join(sorted(str(x**3)))
##        if not z in d: d[z] = [0, y]
##        d[z][0] += 1
##        if d[z][0] == 5: return d[z][1]
