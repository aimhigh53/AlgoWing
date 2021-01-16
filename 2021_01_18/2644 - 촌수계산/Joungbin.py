# 볼 거면 보시고, 아니면 말고...

import sys
from collections import deque

inp = sys.stdin.readline

n = int(inp())
s, e = map(int, inp().split())
m = int(inp())
edge = [[] for _ in range(n + 1)]
dist = [-1] * (n + 1)
for i in range(m):
    x, y = map(int, inp().split())
    edge[x].append(y)
    edge[y].append(x)

q = deque()
q.append(s)
dist[s] = 0

while q:
    a = q.popleft()
    for b in edge[a]:
        if (dist[b] == -1): dist[b] = dist[a] + 1; q.append(b)

print(dist[e])
