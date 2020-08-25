t=int(input())

def quicksort(a) : # l=n(수열의 길이)
    l=len(a)
    if(l<=1) :
        return a
    piv=a[0]
    a1=[]
    a2=[]
    for i in range(1, l) :
        if(a[i]<=piv) :
            a1.append(a[i])
        else :
            a2.append(a[i])
    return quicksort(a1)+[piv]+quicksort(a2)


for tc in range(t) :
    n=int(input())
    a=list(map(int, input().split()))

    print('#%d'%(tc+1), quicksort(a)[n//2])