import heapq

move = [(1,0),(-1,0),(0,-1),(0,1)]

def dijkstra(N, x, y, board):
    ans = 0
    size = 2
    count = 0
    queue = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[x][y] = True
    heapq.heappush(queue, (0, x, y))
    while queue:
        fish, now_x, now_y = heapq.heappop(queue)
        for mx, my in move:
            next_x, next_y = now_x+mx, now_y+my
            if 0 <= next_x < N and 0 <= next_y < N:
                if visited[next_x][next_y]: continue
                visited[next_x][next_y] = True
                if board[next_x][next_y] == 0:
                    board[next_x][next_y] = 1
                    heapq.heappush(queue, (count + 1, next_x, next_y))
                else:
                    heapq.heappush(queue, (count, next_x, next_y))
    return 0
N = int(input())
board = []
for i in range(N):
    board.append(list(map(int,list(input()))))
print(dijkstra(N, 0, 0, board))