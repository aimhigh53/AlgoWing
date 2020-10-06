from collections import deque

Testcase=int(input())


for tc in range(1,1+Testcase):
    tot=0
    N,M=map(int,input().split(' '))
    
    weight=list(map(int,input().split(' ')))
    avail=list(map(int,input().split(' ')))
    
    weight=sorted(weight,reverse=True)
    avail=sorted(avail,reverse=True)
    q=deque(avail)
    
    while q:
        e=q.popleft()
      
        
        for w in weight:
           
            if e>=w:
                tot+=w
                weight.remove(w)
                break

    
    
    print("#{} {}".format(tc,tot))
