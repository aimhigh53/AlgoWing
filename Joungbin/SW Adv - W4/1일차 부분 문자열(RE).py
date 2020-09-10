t=int(input())

for tc in range(t) :
    a=set()
    n, s=map(str, input().split())
    for i in range(len(s)) :
        for j in range(i, len(s)) :
            a.add(s[i:j+1])
    b=list(a)
    b.sort()
    n=int(n)
    print('#%d'%(tc+1), b[n-1][0], len(b[n-1]))