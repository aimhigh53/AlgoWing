from collections import deque

Testcase=int(input())


def sol():
    global cnt
    start,end=0,0
    while q:
        ele=q.popleft()
        start=ele[0]    

        if end<=start:
            cnt+=1
            end=ele[1]

    return cnt
        
    

for tc in range(1,1+Testcase):
    N=int(input())
    cnt=0
    time=[]
    
    for _ in range(N):
        s,e=map(int,input().split(' '))
        time.append((s,e))
        
    time.sort(key=lambda x:x[1])
    q=deque(time)
    
    result=sol()
    
    print('#{} {}'.format(tc,result))
  
        
    
