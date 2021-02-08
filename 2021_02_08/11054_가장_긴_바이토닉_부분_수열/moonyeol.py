import sys
input = sys.stdin.readline

N = int(input())
dp_small = [1 for _ in range(N)]
dp_big = [1 for _ in range(N)]
total = [1 for _ in range(N)]
A = list(map(int,input().split()))
for i in range(1,N):
    for j in range(i):
        if A[i] > A[j]:
            dp_big[i] = max(dp_big[i], dp_big[j]+1)
for i in range(N-2,-1,-1):
    for j in range(N-1,i,-1):
        if A[i] > A[j]:
            dp_small[i] = max(dp_small[i], dp_small[j]+1)
for i in range(N):
    total[i] = dp_big[i] + dp_small[i] -1

print(max(total))