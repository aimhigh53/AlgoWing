from collections import deque

def find_root(N, arr, graph):
    move = [(1,0),(0,1),(-1,0),(0,-1)]
    queue = deque()
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()
        for dx,dy in move:
            nx,ny = x+dx,y+dy
            temp = 0
            if 0<= nx < N and 0<= ny <N :
                if arr[nx][ny] <= arr[x][y]:
                    temp = graph[x][y] + 1
                elif arr[nx][ny] > arr[x][y]:
                    temp = graph[x][y] + 1 + (arr[nx][ny] - arr[x][y])
                if graph[nx][ny] > temp:
                    graph[nx][ny] = temp
                    queue.append((nx,ny))

num = int(input())
TestCases = []
Ns = []
for i in range(num):
    N = int(input())
    Ns.append(N)
    temp = []
    for j in range(N):
        temp.append(list(map(int, input().split())))
    TestCases.append(temp)

for idx, i in enumerate(TestCases):
    answer = 0
    INF = float('inf')
    graph = [[INF for k in range(N)] for a in range(N)]
    graph[0][0] = 0

    find_root(Ns[idx], i, graph)
    print("#" + str(idx + 1) + " " + str(graph[Ns[idx]-1][Ns[idx]-1]))
