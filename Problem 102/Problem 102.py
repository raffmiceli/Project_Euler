def cp(a,b):
    return a[0]*b[1]-a[1]*b[0]

true = 0
for line in open('triangles.txt'):
    tri = [eval(n) for n in line.split(',')]
    a,b,c = tri[:2],tri[2:4],tri[4:]
    ao = [-a[0],-a[1]]
    bo = [-b[0],-b[1]]
    co = [-c[0],-c[1]]
    ab = [(b[0]-a[0]),(b[1]-a[1])]
    ba = [-n for n in ab]
    bc = [(c[0]-b[0]),(c[1]-b[1])]
    cb = [-n for n in bc]
    ac = [(c[0]-a[0]),(c[1]-a[1])]
    ca = [-n for n in ac]
    if cp(ab,ao)*cp(ab,ac) > 0 and\
       cp(bc,bo)*cp(bc,ba) > 0 and\
       cp(ca,co)*cp(ca,cb) > 0:
        true += 1
print true
