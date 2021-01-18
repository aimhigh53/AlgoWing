import collections
import sys
input=sys.stdin.readline

def bfs(x,y):
    q = collections.deque()
    q.append((x,0))
    while q:
        node, count = q.popleft()
        visited[node] = True
        if node == y:
            return count
        for i in graph[node]:
            if visited[i]:
                continue
            q.append((i,count+1))
    return -1


n = int(input())
a, b = map(int,input().split())
m = int(input())
graph = dict()
visited = [False for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    if not x in graph:
        graph[x] = set()
    if not y in graph:
        graph[y] = set()
    graph[y].add(x)
    graph[x].add(y)
print(bfs(a,b))

