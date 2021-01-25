import sys
input=sys.stdin.readline

N = int(input())
stair = []
dp = [0 for _ in range(N)]
for _ in range(N):
    stair.append(int(input()))
if N == 1:
    print(stair[0])
elif N==2:
    print(stair[0] + stair[1])
elif N==3:
    print(max(stair[1] + stair[2], stair[0] + stair[2]))
else:
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    dp[2] = max(stair[1] + stair[2], stair[0] + stair[2])
    for i in range(3, N):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])
    print(dp[N-1])