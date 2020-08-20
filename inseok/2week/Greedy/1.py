        
T=int(input())
 
for case in range(1,T+1):
    N,M=map(int,input().split())
    weight=list(int(x) for x in input().split())
    ton=list(int(y) for y in input().split())
 
    tot=0
    for i in range(len(ton)):
        val=0
        for w in weight:
            if val<=w and w<=ton[i]:
                val=w
        if val!=0:
            weight.remove(val)
        tot+=val
    
    print('#%d #%d'%(case, tot))

