# 미리 넣어둘 테니

import sys

sys.setrecursionlimit(10 ** 9)


def dfs(i, j, h):
    ch[i][j] = 1
    for k in range(4):
        x, y = i + dx[k], j + dy[k]
        if (x < 0 or x >= n or y < 0 or y >= n): continue
        if (ch[x][y] == -1 and mp[x][y] > h): dfs(x, y, h)


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

n = int(input())
mp = [[*map(int, input().split())] for _ in range(n)]
ans = 1

for h in range(1, 101):
    ch = [[-1] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if (ch[i][j] == -1 and mp[i][j] > h): cnt += 1; dfs(i, j, h)
    ans = max(ans, cnt)

print(ans)

# cnt는 높이가 h일 때 안전 영역의 수