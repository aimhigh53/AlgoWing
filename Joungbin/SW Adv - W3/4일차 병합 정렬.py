from collections import deque

def merge_sort(a):
    if len(a)<=1:
        return a

    mid = len(a)//2
    l=merge_sort(a[:mid])
    r=merge_sort(a[mid:])
    return merge(l, r)

def merge(l, r):
    l1=deque(l)
    r1=deque(r)
    res=[]
    global cnt
    if (l1[-1]>r1[-1]):
        cnt+=1
    while(len(l1)>0 and len(r1)>0) :
        if(l1[0]<=r1[0]) :
            res.append(l1.popleft())
        else :
            res.append(r1.popleft())
    if(len(l1)>0) :
        res.extend(l1)
    if(len(r1)>0) :
        res.extend(r1)
    return res

t = int(input())
for tc in range(t):
    n=int(input())
    cnt=0
    a=list(map(int, input().split()))
    a=merge_sort(a)

    print('#%d'%(tc+1), a[n//2], cnt)