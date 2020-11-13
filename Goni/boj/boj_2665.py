from collections import deque

def isBound(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False

n=int(input())
miro=[list(map(int,input())) for i in range(n)]
visited=[[-1]*n for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs():
    queue=deque()
    queue.append([0,0])
    visited[0][0]=0

    while(queue):
        x,y=queue.popleft()
        for i in range(4):
            nowX=x+dx[i]
            nowY=y+dy[i]
            if isBound(nowX,nowY):
                if visited[nowX][nowY]==-1:
                    if miro[nowX][nowY]==0:
                        visited[nowX][nowY]=visited[x][y]+1
                        queue.append([nowX,nowY])
                    else:
                        visited[nowX][nowY]=visited[x][y]
                        queue.appendleft([nowX,nowY])

bfs()
print(visited[n-1][n-1])
