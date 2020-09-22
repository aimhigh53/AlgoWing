#https://mungto.tistory.com/209
#출처에게 항상 무한한 감사를.....

import sys
sys.stdin=open("sample_input.txt",'r')
def makeTree(mid):
    global count
    if mid<=N:
        makeTree(2*mid)
        tree[mid]=count
        count+=1
        makeTree(2*mid+1)

T=int(input())

for test_case in range(1,T+1):
    N=int(input())
    tree=[0]*(N+1)
    count=1
    makeTree(1)

    print("#{} {} {}".format(test_case,tree[1],tree[N//2]))

