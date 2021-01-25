import sys


input = sys.stdin.readline

INF = float('inf')

def find(u):
    if u!=p[u]:
        p[u] = find(p[u])
    return p[u]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    if root1 < root2:
        p[root2] = root1
    else:
        p[root1] = root2

N = int(input())
M = int(input())
p = [i for i in range(N+1)]
ans = 0
for _ in range(M):
    a,b = map(int,input().split())
    if find(a) != find(b):
        union(a, b)

for i in range(2,N+1):
    if find(i) ==1:
        ans +=1

print(ans)