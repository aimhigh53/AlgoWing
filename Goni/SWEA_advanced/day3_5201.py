import sys
sys.stdin=open("sample_input.txt",'r')

T=int(input())

for test_case in range(1,T+1):

    N,M=map(int,input().split())
    w=list(map(int,input().split()))
    t=list(map(int,input().split()))
    w.sort()
    t.sort()
    ans=0

    pivot_w=len(w)-1
    pivot_t = len(t) - 1

    while(pivot_t>=0 and pivot_w>=0):
        if t[pivot_t]<w[pivot_w]:
            pivot_w-=1
        else:
            ans+=w[pivot_w]
            pivot_w-=1
            pivot_t-=1

    print("#", test_case, sep='', end=' ')
    print(ans)


