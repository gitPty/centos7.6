def IPto10(s):
    l=list(map(int,s.split('.')))
    count=0
    for i in range(4):
        count += l[i] *  pow(pow(2,8),4-i-1)
    return count

def toIP(s):
    k=bin(int(s))[2:].zfill(32)
    for i in rang(4):
        ls.append(str(int(k[8*i:8*i+8],2)))
        
    return ".".join(ls)
    
while True:
    try:
        s1=input()
        s2=input()
        print(IPto10(s1))
        print(toIP(s2))
        
    except:
        break
