from math import *
def pythagProd(x):
    y = x/2
    for a in range(1,y+1):
        for b in range(a+1,y+1):
            if sqrt(a**2 + b**2)%1 == 0.0:
                c = sqrt(a**2 + b**2)
                #print(a, b, int(c), int(a+b+c), int(a*b*c))
                if a+b+c == x: return a*b*c
print(pythagProd(1000))

print([[x,y,1000-x-y,x*y*(1000-x-y)] for x in range(1,1000) for y in range(1,x) if x**2+y**2==(1000-x-y)**2])
