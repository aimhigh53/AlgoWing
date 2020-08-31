# 가능한 연산 : +1 -1 *2 -10
from collections import deque

t = int(input())
maxdist = 10**6

def bfs(x):
    global m
    q.append(x)
    dist[x] = 0
    while q:
        y = q.popleft()
        plus1(y)
        minus1(y)
        times2(y)
        minus10(y)
        if(dist[m] != -1):
            return

def plus1(x):
    if(0 <= x + 1 <= maxdist and dist[x + 1] == -1):
        q.append(x + 1)
        dist[x + 1] = dist[x] + 1
def minus1(x) :
    if (0 <= x - 1 <= maxdist and dist[x - 1] == -1):
        q.append(x - 1)
        dist[x - 1] = dist[x] + 1
def times2(x) :
    if (0 <= x * 2 <= maxdist and dist[x * 2] == -1):
        q.append(x * 2)
        dist[x * 2] = dist[x] + 1
def minus10(x) :
    if (0 <= x - 10 <= maxdist and dist[x - 10] == -1):
        q.append(x - 10)
        dist[x - 10] = dist[x] + 1


for tc in range(t):
    n, m = map(int, input().split())
    dist = [-1]*(maxdist+1)
    q = deque()
    bfs(n)
    print('#%d' % (tc+1), dist[m])

