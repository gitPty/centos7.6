import math
while True:
    try:
        n=int(input())
        length= float(n)
        ls=[length]
        k=0
        for i in range(2,6):
            ls.append(length/pow(2,i-1)*2)
        for j in ls:
            k+= j
        print(ls[1]) 
        print("%0.6f"% (length/pow(2,5)))
        print("%0.6f"% k)
    except:
        break
