from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y) :
    global lev, exp, shark_x, shark_y
    q = deque()
    q.append((x, y))
    ch = [[-1]*n for _ in range(n)]
    ch[x][y] = 0
    while q: # 지나갈 수 있는지 없는지, 있다면 거리가 몇 칸인지 판단
        x1, y1=q.popleft()
        for move in range(4):
            nx, ny=x1+dx[move], y1+dy[move]
            if(nx<0 or nx>=n or ny<0 or ny>=n) : continue
            if(ch[nx][ny]==-1 and mp[nx][ny]<=lev):
                ch[nx][ny] = ch[x1][y1]+1
                q.append((nx, ny))
    dist = 10**9
    prey_x, prey_y = 0, 0
    for eat_x in range(n): # 먹이 먹을 수 있는지 판단, 있다면 거리 판단
        for eat_y in range(n):
            if(ch[eat_x][eat_y] != -1) :
                if(lev <= mp[eat_x][eat_y] or mp[eat_x][eat_y] == 0) : continue
                if(ch[eat_x][eat_y] < dist) :
                    prey_x, prey_y = eat_x, eat_y
                    dist = ch[eat_x][eat_y]
    if(dist == 10**9) : # 아무것도 먹을 게 없다면
        return -1
    else:
        mp[prey_x][prey_y] = 0
        shark_x, shark_y = prey_x, prey_y
        if(exp+1 == lev): lev, exp = lev+1, 0
        else : exp += 1
        return dist


n = int(input())
mp = [[*map(int, input().split())] for _ in range(n)]
shark_x, shark_y = 0, 0
lev = 2
exp = 0
ans = 0

for i in range(n) :
    for j in range(n) :
        if(mp[i][j] == 9) :
            shark_x, shark_y=i, j
            mp[i][j] = 0

while True :
    a = bfs(shark_x, shark_y)
    if(a == -1) : break
    ans += a

print(ans)
