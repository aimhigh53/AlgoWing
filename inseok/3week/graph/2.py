# findset
#makeset
#union
from collections import deque


#얘를 어떻게 리턴하냐에 달라짐

# def findset(x): 
#     if x!=subList[x]:
#         findset(subList[x])
#     return subList[x]

def findset(x):
    if x==subList[x]:
        return subList[x]
    else:
        return findset(subList[x])

def union(x,y):
    subList[findset(y)]=findset(x)
    
    
testcase=int(input())

for tc in range(1,testcase+1):
    N,M=map(int,input().split(' '))
    subList=[0]*(N+1)
    ansList=[]
    numberList=list(map(int,input().split(' ')))
    
    #여기,,
    for i in range(1,N+1):
        subList[i]=i
    
    for i in range(M):
        front=numberList[2*i]
        back=numberList[2*i+1]
        union(front,back)
    
    for i in range(N+1):
        ansList.append(findset(i))
    
    print('#{} {}'.format(tc,len(set(ansList))-1))

