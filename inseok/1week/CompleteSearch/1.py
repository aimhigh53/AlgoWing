M=int(input())

dx=[0,1]
dy=[1,0]
cnt=0


def sol(i,j,N,arr,check,anslist):
    check[0][0]=arr[0][0]
    tmp=check[i][j]
    if i==N-1 and j==N-1:
        anslist.append(check[i][j])
        return 
        
    for k in range(2):
        if i+dx[k]<N and j+dy[k]<N and check[i+dx[k]][j+dy[k]]>0:
            if check[i+dx[k]][j+dy[k]]>arr[i+dx[k]][j+dy[k]]+tmp:
                check[i+dx[k]][j+dy[k]]=arr[i+dx[k]][j+dy[k]]+tmp
                sol(i+dx[k],j+dy[k],N,arr,check,anslist)
                
        elif i+dx[k]<N and j+dy[k]<N and check[i+dx[k]][j+dy[k]]==0:
            check[i+dx[k]][j+dy[k]]=check[i][j]+arr[i+dx[k]][j+dy[k]]
            sol(i+dx[k],j+dy[k],N,arr,check,anslist)
        
                

    
#     print('#%d',num)
    
    

while M>0:
    cnt+=1
    anslist=[]
    N=int(input())
    arr=[0 for y in range(N)]
    check=[[0]*N for z in range(N)]
    for k in range(N):
        arr[k]=[int(x) for x in input().split()]

    sol(0,0,N,arr,check,anslist)
    print("#%d"%(cnt),min(anslist))
    M-=1
                
        
        
