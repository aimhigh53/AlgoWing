t=int(input())

for tc in range(t) :
    m=list(map(int, input().split()))
    a=[0]*10
    b=[0]*10
    ans=0
    for i in range(6) :
        a[m[2*i]]+=1
        if(3 in a) : ans=1; break
        for j in range(8) :
            if(a[j]>0 and a[j+1]>0 and a[j+2]>0) : ans=1; break
        if(ans!=0):
             break
        b[m[2*i+1]]+=1
        if(3 in b) : ans=2; break
        for j in range(8) :
            if(b[j]>0 and b[j+1]>0 and b[j+2]>0): ans=2; break
        if(ans!=0) :
            break
    print('#%d'%(tc+1), ans)