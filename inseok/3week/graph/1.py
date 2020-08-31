#tc
#연산은 +1,-1,*2,-10
from collections import deque
#bfs

def cal(i,val):
    global cnt
    if i==0:
        val+=1
    elif i==1:
        val-=1
    elif i==2:
        val*=2        
    elif i==3:
        val-=10

    return val

def bfs(N):
    global cnt
    global tc
    dq.append((N,0))
    anslist[N]=tc
    while dq:
#         print(dq)
        temp,cnt=dq.popleft()
#         if temp==M:
#             return cnt
        for i in range(4):
            val=cal(i,temp)
            if val==M:
                return cnt+1
            elif 1<=val<=1000000 and anslist[val]!=tc:
                #저 리스트때문에 runtimeerror
                dq.append((val,cnt+1))
                anslist[val]=tc
                
    
    #연산 여러가지 
testcase=int(input())
anslist=[0]*1000001
for tc in range(1,testcase+1):
    N,M=map(int,input().split(' '))
    dq=deque()
    cnt=0
    print('#{} {}'.format(tc,bfs(N)))
    
