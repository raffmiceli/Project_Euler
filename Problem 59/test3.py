import time
t1=time.time()
cipher=[]
decipher=""
key=['a','a','a']
pc="abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ.-,1234567890'~!$%^&()_+;:?><|\ "#PC stands for possible characters
#Opening file
f=open("cipher1.txt").readlines()
for line in f:
    for token in line.replace("\n","").split(','):
        cipher.append(int(token))
#Finding key
for i in range(len(cipher)):
        while(pc.count(chr(ord(key[i%3])^cipher[i]))==0):
            key[i%3]=chr(ord(key[i%3])+1) #increase the ascci value of letters until a printable character is found
#Decoding
asciisum=0
for i in range(len(cipher)):
          decipher+=chr(cipher[i]^ord(key[i%3]))
          asciisum+=cipher[i]^ord(key[i%3])
print("Key = ",key[0],key[1],key[2])
print("Ascii sum =",asciisum)
print("And the deciphered text is..\n",decipher)
print("Time taken:",time.time()-t1,"sec")
