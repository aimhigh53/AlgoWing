t=int(input())

def dfs(x) :
    ch[x]=1
    for y in g[x] :
        if(ch[y]==0) :
            dfs(y)

for tc in range(t) :
    n, m=map(int, input().split())
    a=list(map(int, input().split()))
    g=[[] for _ in range(n+1)]
    ch=[0]*(n+1)
    ans=0
    for i in range(m) :
        x, y=a[2*i], a[2*i+1]
        g[x].append(y)
        g[y].append(x)
    for i2 in range(1, n+1) :
        if(ch[i2]==0) :
            dfs(i2)
            ans+=1
    # print(ch)
    print('#%d'%(tc+1), ans)