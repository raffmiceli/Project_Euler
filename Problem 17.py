def numWords(n):
    l1 = ['zero','one','two','three','four','five','six','seven','eight','nine','ten',\
          'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    l2 = ['zero','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

    if n <= 19:
        return l1[n]
    elif n < 100:
        if n%10 == 0:
            return l2[int(str(n)[0])]
        ones = int(str(n)[1])
        tens = int(str(n)[0])
        return l2[tens]+l1[ones]
    elif n < 1000:
        if n%100 == 0:
            return l1[int(str(n)[0])]+'hundred'
        hundreds = int(str(n)[0])
        rest = int(str(n)[1:])
        return l1[hundreds]+'hundredand'+numWords(rest)
    elif n == 1000:
        return 'onethousand'
t = 0

for n in range(1,1001):
    x = numWords(n)
    l = len(x)
    #print n, x, l
    t += l
print t

def numWDict():
    s={0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six"/
    ,7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven"/
    ,12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen"/
    ,16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"/
    ,20:"twenty",30:"thirty",40:"forty",50:"fifty"/
    ,60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
    for i in range(1,1000):
        if(not i in s.keys()):
            if(i<100):
                s[i]=s[i/10*10]+s[i%10]

        else:
            s[i]=s[i/100]+"hundred"
            if(i%100):
                s[i]+="and"+s[i%100]
    s[1000]="onethousand"
    total=0;
    for i in s.values():
        total+=len(i)
