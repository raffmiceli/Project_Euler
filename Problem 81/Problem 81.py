f = open('matrix.txt', 'r')
g = [[int(n) for n in line.split(',')] for line in f.readlines()]
f.close()
matrix = {(a,b):g[a][b] for a in xrange(80) for b in xrange(80)}

def minpath2(matrix):
    dist = {(a,b):10**6 for a in xrange(80) for b in xrange(80)}
    dist[(0,0)] = matrix[(0,0)]
    Q = [(a,b) for a in xrange(80) for b in xrange(80)]
    keys = matrix.keys()
    while len(Q):
        mi = 10**6
        u = (0,0)
        for key in Q:
            if dist[key] < mi:
                u,mi = key,dist[key]
        Q.remove(u)
        if u == (79,79): break
        neighbors = [(u[0]+1, u[1]),(u[0],u[1]+1)]
        for v in neighbors:
            if v not in keys: continue
            alt = dist[u] + matrix[v]
            if alt < dist[v]:
                dist[v] = alt
    return dist[u]

print minpath2(matrix)

a = g[:]
b = [[0 for m in xrange(80)] for n in xrange(80)]
b[0][0] = a[0][0]

for i in xrange(1,80):
    b[0][i] = a[0][i]+b[0][i-1]
    b[i][0] = a[i][0]+b[i-1][0]
for i in xrange(1,80):
    for j in xrange(1,80):
        b[i][j] = a[i][j]+min(b[i-1][j],b[i][j-1])
print b[79][79]
