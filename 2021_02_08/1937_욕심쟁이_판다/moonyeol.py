import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

moving = [(1, 0), (-1, 0), (0, 1), (0, -1)]
K = 0

def move(x, y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    global K
    for mx, my in moving:
        nx, ny = x + mx, y + my
        if 0 <= nx < n and 0 <= ny < n:
            if woods[nx][ny] > woods[x][y]:
                dp[x][y] = max(dp[x][y],move(nx,ny)+1)
    if dp[x][y] > K:
        K = dp[x][y]
    return dp[x][y]

n = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]
woods = []
for _ in range(n):
    woods.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        move(i, j)
print(K)