from itertools import *
from math import sqrt, log
from fractions import gcd
import time

def find((m1, n1), (m2, n2), N):
    if m1 == m2 - 1 and n2 > N:
        return (m2, n2)
    else:
        # n = cm^d
        # n1 = cm1^d
        # n2 = cm2^d
        # n2/n1 = (m2/m1)^d
        # d = log(n2/n1) / log(m2/m1)
        # c = m1^d / n1
        d = log(float(n2) / n1) / log(float(m2) / m1)
        c = n1 / m1 ** d
        m3 = int((N / c) ** (1 / d) + 0.5)
        if n2 < N:
            m3 = min(m3, int(m2 * 2))
            return find((m2, n2), (m3, num_cuboids(m3)), N)
        else:
            if m3 == m1:
                m3 += 1
            elif m3 == m2:
                m3 -= 1
            n3 = num_cuboids(m3)
            if n3 <= N:
                return find((m3, n3), (m2, n2), N)
            else:
                return find((m1, n1), (m3, n3), N)

# [a/2] + [2a/2] + ... + [na/2]
def sum_half(a, n):
    if a % 2 == 0:
        return a * n * (n + 1) / 4
    else:
        return (a * n * (n + 1) / 2 - (n + 1) / 2) / 2

def num_cuboids(M):
    def f(a, b):
        l1 = M / b
        s1 = sum_half(a, l1)
        l2 = M / a
        d = a - b / 2
        if d <= 0:
            s2 = 0
        elif b % 2 == 0:
            s2 = d * l2 * (l2 + 1) / 2 + l2
        else:
            s2 = a * l2 * (l2 + 1) / 2 - sum_half(b, l2) + l2 / 2
        
        return s1 + s2
    
    return sum(f(a, b) for a, b in gen_ab(M))

def gen_ab(M):
    for m, n in gen_mn(M):
        a = 2 * m * n
        b = m * m - n * n
        if a < b:
            yield a, b
        else:
            yield b, a

def gen_mn(M):
    f = 1 + sqrt(2)
    for m in xrange(2, int(sqrt(f * M)) + 1):
        n0_tmp = int(sqrt(max(1, m * m - M * 2)))
        n0 = n0_tmp + (1 if (m + n0_tmp) % 2 == 0 else 0)
        for n in xrange(n0, min(m, M / m + 1), 2):
            if gcd(m, n) == 1:
                yield m, n

def solve(N):
    return find((4, num_cuboids(4)), (8, num_cuboids(8)), N)

for e in xrange(6, 14):
    N = 10 ** e
    t0 = time.clock()
    n, _ = solve(N)
    t1 = time.clock()
    print "10^%d => %d %.3fs" % (e, n, t1 - t0)
