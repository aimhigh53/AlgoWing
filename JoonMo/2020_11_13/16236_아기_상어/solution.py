# 정말 시간 많이 날린 문제
# heaqp를 사용해줘야 왼쪽 위쪽 에 있는 물고기 우선순위를 고려해줄 수 있다
# 자기보다 큰 물고기로 둘러쌓여있을 경우를 생각해주지 못하면
# haepq가 비어있기 때문에 에러가 뜬다


from collections import deque
import heapq

# 맵 출력
def grid_prnt(grid):
    for i in grid:
        print(i)

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# grid_prnt(grid)

# 맵을 확인해서 작은 물고기가 있으면 True 없으면 False
def check_help(shark_size):
    for y in range(N):
        for x in range(N):
            if grid[y][x] !=0 and grid[y][x] < shark_size:
                return True
    return False

dx = [0,-1,1,0]
dy = [-1,0,0,1]

def InBound(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    else:
        return False

def bfs(x,y):
    global shark_size
    global eat

    q = deque()
    q.append((x,y,0))
    visited = [(x,y)]
    closest = []

    while q:
        smallest_time = float('inf')
        curr_x, curr_y, curr_time = q.popleft()

        # if curr_time > smallest_time:
        #     return closest[0]

        # print('현재', curr_x, curr_y)
        for i in range(4):
            next_x = curr_x + dx[i]
            next_y = curr_y + dy[i]
            if InBound(next_x, next_y):
                if (next_x, next_y) not in visited:
                    # 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고
                    if grid[next_y][next_x] > shark_size:
                        continue
                    
                    # 자신의 크기보다 작은 물고기만 먹을 수 있다.
                    elif grid[next_y][next_x] < shark_size and grid[next_y][next_x] != 0:
                        heapq.heappush(closest, (curr_time+1, next_y, next_x))
                        visited.append((next_x, next_y))
                    
                    else:
                        q.append((next_x, next_y, curr_time + 1))
                        visited.append((next_x, next_y))
        # q = deque(sorted(q, key = lambda x : (x[2], x[1], x[0])) )
        # print(q)
    if closest:
        time, next_y, next_x = closest[0]
        eat += 1
        if eat == shark_size:
            shark_size += 1
            eat = 0
        grid[next_y][next_x] = 0

        # print(closest)
        return closest[0]

    else:
        return -1, 0, 0


def find_shark(grid):
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 9:
                grid[y][x] = 0
                return x, y

# 시작시간
time = 0
# 시작 상어 크기
global shark_size
global eat
shark_size = 2
eat = 0

# 아기 상어 위치 확인
start_x, start_y = find_shark(grid)

# 아기 상어가 먹을 물고기가 없을때까지 반복
while check_help(shark_size):
    # 아기상어 위치에서 가장 가까운 고기 확인
    # print(start_x, start_y)
    tmp_time, start_y, start_x = bfs(start_x, start_y)

    if tmp_time == -1:
        break
    time += tmp_time

    # print('shark size', shark_size)
    # print(time)
    # print()

print(time) 
