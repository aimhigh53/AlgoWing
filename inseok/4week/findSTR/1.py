Testcase=int(input())
 
 
def sol():
    #KMP
    cnt=0
    for i in AList:
    	if i in BList:
    		cnt+=1
 
    return cnt
 
 
 
for tc in range(1,1+Testcase):
    N,M=map(int,input().split(' '))
 
    AList=[]
    BList=[]
 
    for _ in range(N):
        AList.append(input())
 
    for _ in range(M):
        BList.append(input())
 
    cnt=sol()
    print('#{} {}'.format(tc,cnt))
 
