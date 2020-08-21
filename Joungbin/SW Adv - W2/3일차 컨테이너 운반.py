t=int(input())

for tc in range(t) :
    n, m=map(int, input().split()) # 컨테이너 수, 트럭 수
    a=list(map(int, input().split()))
    a.sort()
    b=list(map(int, input().split()))
    b.sort()
    ans=0
    for i in range(min(n, m)) :
        if(a[len(a)-1]<=b[len(b)-1]) :
            ans+=a[len(a)-1]
            b.pop()
        a.pop()
    print('#%d'%(tc+1), ans)