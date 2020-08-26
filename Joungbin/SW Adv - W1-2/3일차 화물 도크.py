t=int(input())

for tc in range(t) :
    n=int(input())
    a=[]
    ans=0
    for i in range(n) :
        a.append(list(map(int, input().split())))
    a.sort(key=lambda x : x[0])
    a.sort(key=lambda x : x[1])
    st=a[0][0]
    for i in range(n) :
        if(st<=a[i][0]) :
            st=a[i][1]
            ans+=1
    print('#%d'%(tc+1), ans)