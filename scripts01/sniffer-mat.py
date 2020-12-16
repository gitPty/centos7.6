while True:
    try:
        n=int(input())
        res=[[ 0 for i in range(n)] for i in range(n)]
        k=1
        for i in range(n):
            for j in range(i+1):
                res[i-j][j]=k
                k+=1
        for i in res:
            print(" ".join(map(str,filter(lambda x:x!=0 ,x))))
            
            
    except:
        break
