t=int(input())

for tc in range(t) :
    n, m=map(int, input().split())
    a=set()
    b=set()
    for i in range(n) :
        a.add(input())
    for i in range(m) :
        b.add(input())
    print('#%d'%(tc+1), len(a&b))