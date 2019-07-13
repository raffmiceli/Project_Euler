##l1 = ['0','1','2','3','4','5','6','7','8','9']
##t = 0
##
##for a in l1:
##    if a != '0':
##        l2 = [a]
##        for b in list(set(l1) - set(l2)):
##            l2 = [a,b]
##            for c in list(set(l1) - set(l2)):
##                l2 = [a,b,c]
##                for d in list(set(l1) - set(l2)):
##                    l2 = [a,b,c,d]
##                    for e in list(set(l1) - set(l2)):
##                        l2 = [a,b,c,d,e]
##                        for f in list(set(l1) - set(l2)):
##                            l2 = [a,b,c,d,e,f]
##                            for g in list(set(l1) - set(l2)):
##                                l2 = [a,b,c,d,e,f,g]
##                                for h in list(set(l1) - set(l2)):
##                                    l2 = [a,b,c,d,e,f,g,h]
##                                    for i in list(set(l1) - set(l2)):
##                                        l2 = [a,b,c,d,e,f,g,h,i]
##                                        for j in list(set(l1) - set(l2)):
##                                            n = a+b+c+d+e+f+g+h+i+j
##                                            if int(n[1:4])%2 == 0:
##                                                if int(n[2:5])%3 == 0:
##                                                    if int(n[3:6])%5 == 0:
##                                                        if int(n[4:7])%7 == 0:
##                                                            if int(n[5:8])%11 == 0:
##                                                                if int(n[6:9])%13 == 0:
##                                                                    if int(n[7:10])%17 == 0:
##                                                                        print n
##                                                                        t += int(n)
##print t

l1 = ['0','1','2','3','4','5','6','7','8','9']
t = 0

for a in l1:
    if a != '0':
        l2 = [a]
        for b in list(set(l1) - set(l2)):
            l2 = [a,b]
            for c in list(set(l1) - set(l2)):
                l2 = [a,b,c]
                for d in list(set(l1) - set(l2)):
                    l2 = [a,b,c,d]
                    if int(b+c+d)%2 == 0:
                        for e in list(set(l1) - set(l2)):
                            l2 = [a,b,c,d,e]
                            if int(c+d+e)%3 == 0:
                                for f in list(set(l1) - set(l2)):
                                    l2 = [a,b,c,d,e,f]
                                    if int(d+e+f)%5 == 0:
                                        for g in list(set(l1) - set(l2)):
                                            l2 = [a,b,c,d,e,f,g]
                                            if int(e+f+g)%7 == 0:
                                                for h in list(set(l1) - set(l2)):
                                                    l2 = [a,b,c,d,e,f,g,h]
                                                    if int(f+g+h)%11 == 0:
                                                        for i in list(set(l1) - set(l2)):
                                                            l2 = [a,b,c,d,e,f,g,h,i]
                                                            if int(g+h+i)%13 == 0:
                                                                for j in list(set(l1) - set(l2)):
                                                                    if int(h+i+j)%17 == 0:
                                                                        n = a+b+c+d+e+f+g+h+i+j
                                                                        #print n
                                                                        t += int(n)
print t

##print(sum([int(n) for n in map(lambda x: ''.join(x), permutations("1234567890")) if all(int(n[i:i+3])%[2,3,5,7,11,13,17][i-1] == 0 for i in range(1,8))]))
