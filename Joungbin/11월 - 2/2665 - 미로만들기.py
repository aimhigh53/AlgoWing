from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

n = int(input())
mp = [[int(i) for i in input()] for _ in range(n)]
ch = [[0]*n for _ in range(n)]
dist = [[-1] * n for _ in range(n)]
dist[0][0] = 0

q = deque()
q.append((0, 0))
ch[0][0] = 1
while q:
    x, y = q.popleft()
    for i in range(4) :
        nx, ny=x+dx[i], y+dy[i]
        if(nx<0 or nx>=n or ny<0 or ny>=n) : continue
        if(mp[nx][ny] == 1 and (dist[nx][ny] == -1 or dist[nx][ny] > dist[x][y])) :
            # 1이면 안 부수고 그냥 이동 가능
            dist[nx][ny]=dist[x][y]
            q.append((nx, ny))
        elif(mp[nx][ny]==0 and (dist[nx][ny] == -1 or dist[nx][ny] > dist[x][y] + 1)) :
            # 0이면 부숴야 이동 가능
            dist[nx][ny]= dist[x][y] + 1
            q.append((nx, ny))

print(dist[-1][-1]) # 맨 끝 점