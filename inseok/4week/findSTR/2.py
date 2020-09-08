Testcase=int(input())
 
def sol():
     
    cnt=0
    for i in BList:
        switch=False
        for j in AList:

            if j.find(i)==0:

                switch=True
                
        if switch:
            cnt+=1
            
    return cnt
 
for tc in range(1,Testcase+1):
    N,M=map(int,input().split(' '))
    AList=[]
    BList=[]
 
    for _ in range(N):
        AList.append(input())
 
    for _ in range(M):
        BList.append(input())
 
    cnt=sol()
    print('#{} {}'.format(tc,cnt))
