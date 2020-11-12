import collections
import heapq
import sys
move = [(1,0),(-1,0),(0,-1),(0,1)]
input = sys.stdin.readline
def find_min(N, x, y, board, size):
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[x][y] = True
    minDist = []
    board[x][y] = 0
    queue = collections.deque()
    queue.append([0, x, y])
    while queue:
        count, now_x, now_y = queue.popleft()
        for mx, my in move:
            next_x, next_y = now_x + mx, now_y + my
            if 0 <= next_x < N and 0 <= next_y < N:
                if visited[next_x][next_y]: continue
                visited[next_x][next_y] = True
                if board[next_x][next_y] == size or board[next_x][next_y] ==0:
                    queue.append([count+1,next_x,next_y])
                elif board[next_x][next_y] < size:
                    heapq.heappush(minDist, (count + 1, next_x, next_y))
    if minDist:
        return minDist[0]
    return -1

def solution(N, x, y, board):
    size = 2
    time = 0
    count_fish = 0
    while True:
        next = find_min(N, x, y, board, size)
        if next == -1:
            break
        count, now_x, now_y = next
        time += count
        count_fish +=1
        if count_fish == size:
            size +=1
            count_fish =0
        x, y= now_x, now_y
    return time





N = int(input())
board = []
for i in range(N):
    board.append(list(map(int,input().split())))

x,y = 0,0
for i in range(N):
    is_find = False
    for j in range(N):
        if board[i][j] == 9:
            x,y = i, j
            is_find = True
            break
    if is_find:
        break

print(solution(N,x,y,board))