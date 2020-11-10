dx=[-1, 0, 0, 1]
dy=[0, -1, 1, 0]

n, m=map(int, input().split())
a=[[str(i) for i in input()] for _ in range(n)]
ch=[[0]*m for _ in range(n)]
cnt=0
mod=10**9+7


for i in range(n) :
    for j in range(m) :
        for k in range(4) :
            x, y=i+dx[k], j+dy[k]
            if(x<0 or x>=n or y<0 or y>=m) : continue
            if(a[x][y]!=a[i][j]) :
                if(ch[i][j]==0 and ch[x][y]==0) : cnt+=2
                elif(ch[i][j]==0 or ch[x][y]==0) : cnt+=1
                ch[x][y]=ch[i][j]=1
        ch[i][j]=1

print(2**(n*m-cnt))