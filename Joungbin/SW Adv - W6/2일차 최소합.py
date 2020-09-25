t = int(input())
dx = [0, 1]
dy = [1, 0]

for tc in range(t):
    n = int(input())
    board = []
    cost = [[0] * n for _ in range(n)]
    for row in range(n):
        board.append(list(map(int, input().split())))
    cost[0][0] = board[0][0]
    for row in range(n):
        for column in range(n):
            for k in range(2):
                x, y = row + dx[k], column + dy[k]
                if(0<=x<n and 0<=y<n):
                    if(cost[x][y] == 0 or cost[x][y] > cost[row][column] + board[x][y]):
                        cost[x][y] = cost[row][column] + board[x][y]
    print('#%d' % (tc+1), cost[n - 1][n - 1])
