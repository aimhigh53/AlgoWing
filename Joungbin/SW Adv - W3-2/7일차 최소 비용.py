from collections import deque

t = int(input())

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y):
    q = deque()
    dist[x][y] = 0
    q.append((x, y))
    while q:
        before_x, before_y = q.popleft()
        for direction in range(4):
            new_x, new_y = before_x + dx[direction], before_y + dy[direction]
            if(new_x < 0 or new_x >= n or new_y < 0 or new_y >= n):
                continue
            if(mp[new_x][new_y] <= mp[before_x][before_y]):
                fuel = 0 # 높이 차에 의해 소비되는 연료
            else:
                fuel = mp[new_x][new_y]-mp[before_x][before_y]
            if(dist[new_x][new_y] == -1 or dist[new_x][new_y] > dist[before_x][before_y] + 1 + fuel):
                    dist[new_x][new_y] = dist[before_x][before_y] + 1 + fuel
                    q.append((new_x, new_y))


for tc in range(t) :
    n = int(input())
    mp = [] # 지도
    dist = [[-1]*n for _ in range(n)]
    for mp_input in range(n):
        mp.append(list(map(int, input().split())))
    bfs(0, 0)
    print('#%d'%(tc+1), dist[-1][-1])