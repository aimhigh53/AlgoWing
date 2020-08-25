import sys
sys.stdin=open("sample_input.txt","r")

def binary(num):
    global ans
    past=None
    l=0
    r=len(A)-1

    while(l<=r):
        pivot=(l+r)//2
        if num==A[pivot]:
            ans+=1
            return
        elif num>A[pivot]:
            l=pivot+1
            if past=="right":
                return
            now="right"
        elif num<A[pivot]:
            r=pivot-1
            if past=="left":
                return
            now="left"
        past=now

T=int(input())
for test_case in range(1,T+1):
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    B=list(map(int,input().split()))
    ans=0

    for i in B:
        binary(i)


    print("#",test_case,sep='',end=' ')
    print(ans)


