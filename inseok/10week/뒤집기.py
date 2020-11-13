N,M=map(int,input().split())
field=[[0 for _ in range(M)]for _ in range(N)]

for i in range(N):
    field[i]=list(input())

dx=[1,0,-1,0]
dy=[0,1,0,-1]

cnt=0
ans=1

for i in range(N):
    for j in range(M):
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            
            if nx>=0 and nx<N and ny>=0 and ny<M:
                if field[i][j]!=field[nx][ny]:
                    cnt+=1
                    break
                    
ans=pow(2,N*M-cnt)%1000000007
print(ans)
