import math


def rsa_encrypt(p,q,str):
    n = p*q
    z = (p-1)*(q-1)
    for e in range(2,n-1):
        if z % e != 0:          ## and (z) % e != 0:
            break
    #print(e)
    for d in range(z+n,2,-1):
        if (e*d-1)%z == 0:
            break
    #print(d) 
    newStr=""
    for x in str:
        i = 0
        m = pow(ord(x),e)%n
    
        newStr=newStr + chr(m)
        i+=1

    return newStr

    # tempStr = ""
    # for x in newStr:
    #     c = pow(ord(x),d)%n
    #     tempStr += chr(c)
        
    # print(tempStr)

num1 = 11
num2 = 13
print("Enter String:")
str = input()

newStr = rsa_encrypt(num1,num2,str)
print("Encryption:"+ newStr)

