def islegal(IP):
    ls=IP.split('.')
    flag=True
    for i in ls:
        try:
            if int(i)>255 and int(i)<0:
                flag= False
                break
        except:
            flag= False
            break
    return flag
print(islegal('192.132.44.256'))
