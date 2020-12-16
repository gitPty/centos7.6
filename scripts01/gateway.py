def islegal(IP):
    ls=IP.split('.')
    for i in ls:
        try: 
            if int(i)>256 and int(i)<0:
                return False
        except:
            return False
    return True
def gateway(mask,IP):
    ls1=list(map(int,mask.split('.')))
    ls2=list(map(int,IP.split('.')))
    ls=[]
    for i in range(4):
        ls += [ls1[i] & ls2[i]]
    return ".".join(ls)

while True:
    try:
        mask=input()
        IP1=input()
        IP2=input()
        
        if islegal(mask) and  islegal(IP1) and  islegal(IP2):
            s1=gateway(mask,IP1)
            s2=gateway(mask,IP2)
            if s1 == s2:
                print(0)
            else:
                print(2)
                
        else:
            print(1)
            
    except:
        break
