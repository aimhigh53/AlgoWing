import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)
#INF = sys.maxsize
INF = float('inf')
def solution(x, visited):
    global W
    global N
    global dp
    if visited == (1 << N)-1 :
        if W[x][0] == 0:
            return INF
        else:
            return W[x][0]
    if dp[x][visited] != INF:
        return dp[x][visited]
    for newY in range(1,N):
        if W[x][newY] == 0 or (visited & 1 << newY):
            continue
        dp[x][visited] = min(dp[x][visited], solution(newY, visited | 1 << newY) + W[x][newY])
    return dp[x][visited]


N = int(input())
W = []
visited = (1 << N) | 1
dp = [[INF]*(1<<N) for _ in range(N)]
print(dp)
for i in range(N):
    W.append(list(map(int, input().split())))

answer = solution(0, 1)
print(answer)




'''
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)
#INF = sys.maxsize
INF = float('inf')
def solution(x, y, visited):
    global W
    global N
    global dp
    if visited == (1 << N+1)-1 :
        if W[x][0] == 0:
            return INF
        else:
            return W[x][0]
    if dp[x][y] != INF:
        return dp[x][y]
    for newY in range(1,N):
        if W[x][newY] == 0 or (visited & 1 << newY):
            continue
        dp[x][y] = min(dp[x][y], solution(newY, y, visited | 1 << newY) + W[x][newY])
    return dp[x][y]


N = int(input())
W = []
visited = (1 << N) | 1
dp = [[INF for _ in range(N)] for _ in range(N)]
for i in range(N):
    W.append(list(map(int, input().split())))

answer = solution(0, 0, visited)
print(answer)
'''