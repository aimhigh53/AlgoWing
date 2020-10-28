# 순열과 큐 사용, 재귀를 사용할 경우 더 깔끔해질 듯.

from itertools import permutations
from collections import deque

op=[]
num=[]
s=input()
x=''
ans=0

for i in s :
    if(i.isdigit()==False) :
        op.append(i)
        num.append(x)
        x=''
    else :
        x+=i
num.append(x)

opset=set(op)
opperm=list(permutations(opset, len(opset)))

for i in range(len(opperm)) :
    numqueue=deque(num)
    opqueue=deque(op)
    for j in range(len(opset)) :
        l=len(opqueue)
        for k in range(l) :
            if(opqueue[0]==opperm[i][j]) :
                if(len(opqueue)!=l) :
                    numqueue.append(str(eval(numqueue.pop()+opqueue[0]+numqueue[0])))
                else :
                    numqueue.append(str(eval(numqueue[0]+opqueue[0]+numqueue[1])))
                    numqueue.popleft()
                numqueue.popleft()
                opqueue.popleft()
            else :
                numqueue.append(numqueue.popleft())
                opqueue.append(opqueue.popleft())
    fin=numqueue[0]
    if(ans<abs(int(fin))) :
        ans=abs(int(fin))

print(ans)