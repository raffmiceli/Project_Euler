f = open('triangle.txt', 'r')
tri = [[int(n) for n in line.split(' ')] for line in f]
f.close()

while len(tri) > 1:
    for n in range(len(tri[-2])):
        tri[-2][n] += max(tri[-1][n:n+2])
    tri.pop()
print tri[0][0]
