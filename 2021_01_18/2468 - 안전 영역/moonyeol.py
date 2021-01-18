import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

move = [(-1,0),(1,0),(0,-1),(0,1)]

def dfs(rain, x, y):
    visited[x][y] = True
    if matrix[x][y] <= rain:
        return
    for mx, my in move:
        nx, ny = x + mx, y + my
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            dfs(rain,nx, ny)

ans = 0
N = int(input())
matrix = []
max_n = 0
for _ in range(N):
    temp = list(map(int,input().split()))
    matrix.append(temp)

max_n = max(map(max,matrix))

for n in range(0,max_n):
    count = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            if matrix[i][j] <= n:
                visited[i][j] = True
            elif matrix[i][j] > n:
                dfs(n,i,j)
                count += 1

    ans = max(ans,count)
print(ans)
