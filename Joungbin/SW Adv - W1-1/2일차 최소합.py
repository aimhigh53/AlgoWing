t=int(input())
dx=[0, 1]
dy=[1, 0]

for tc in range(t) :
    n=int(input())
    a=[]
    s=[[0]*n for _ in range(n)]
    for i in range(n) :
        a.append(list(map(int, input().split())))
    s[0][0]=a[0][0]
    for i in range(n) :
        for j in range(n) :
            for k in range(2) :
                x, y=i+dx[k], j+dy[k]
                if(0<=x<n and 0<=y<n) :
                    if(s[x][y]==0 or s[x][y]>s[i][j]+a[x][y]) :
                        s[x][y]=s[i][j]+a[x][y]
    print('#%d'%(tc+1), s[n-1][n-1])