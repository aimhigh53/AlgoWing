t=int(input())

for tc in range(t) :
    a=list(map(int, input().split()))
    n=a.pop(0)
    d=[-1]*n # 처음에는 기본값으로 시작하므로 거리를 -1로 설정

    for i in range(n-1) :
        k=a[i]
        for j in range(1, k+1) :
            if(i+j<n and (d[i+j]==-1 or d[i+j]>d[i]+1)) : # 범위를 넘지 않는 선에서 거리를 검사
                d[i+j]=d[i]+1
    
    print('#%d'%(tc+1), d[-1])
