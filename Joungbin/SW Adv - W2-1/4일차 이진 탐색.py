t=int(input())

for tc in range(t) :
    n, m=map(int, input().split())
    a=sorted(list(map(int, input().split())))
    b=list(map(int, input().split()))

    ans=0
    for i in range(len(b)) :
        l, r = 0, n-1
        ch=0
        while(l<=r) :
            mid=(l+r)//2
            if(b[i]==a[mid]) :
                ans+=1
                break
            else :
                if(b[i]<a[mid]) :
                    if(ch==-1) :
                        break
                    r=mid-1
                    ch=-1
                else :
                    if(ch==1) :
                        break
                    l=mid+1
                    ch=1
    print('#%d'%(tc+1), ans)