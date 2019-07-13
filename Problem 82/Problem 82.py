f = open('matrix.txt', 'r')
g = [[int(n) for n in line.split(',')] for line in f.readlines()]
f.close()
matrix = {(a,b):g[a][b] for a in xrange(80) for b in xrange(80)}

def minpath3(matrix):
    minpaths = []
    for n in xrange(80):
        #print n,
        dist = {(a,b):10**6 for a in xrange(80) for b in xrange(80)}
        dist[(n,0)] = matrix[(n,0)]
        Q = [(a,b) for a in xrange(80) for b in xrange(80)]
        keys = matrix.keys()
        n = 0
        vis = []
        while len(Q):
            mi = 10**6
            u = (0,0)
            for key in Q:
                if dist[key] < mi:
                    u,mi = key,dist[key]
            if n == 1 and u[1] == 0: break
            if len(minpaths) > 0:
                if dist[u] > min(minpaths): break
            Q.remove(u)
            if u[1] == 79:
                minpaths.append(dist[u])
                #print dist[u]
                break
            if u in vis: break
            vis.append(u)
            neighbors = [(u[0]+1, u[1]),(u[0],u[1]+1),(u[0]-1,u[1])]
            for v in neighbors:
                if v not in keys: continue
                alt = dist[u] + matrix[v]
                if alt < dist[v]:
                    dist[v] = alt
            n += 1
    return min(minpaths)

print minpath3(matrix)
