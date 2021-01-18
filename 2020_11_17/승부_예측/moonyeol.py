move = [(-1,0),(0,-1),(1,0),(0,1)]


def solve(N, M, board):
    count = 0
    for x in range(N):
        for y in range(M):
            for mx, my in move:
                nx,ny = x + mx, y +my
                if 0 <= nx < N and 0 <= ny < M:
                    if board[x][y] != board[nx][ny]:
                        count+=1
                        break
    return 2**(N*M - count)

ans = 0
N, M = map(int,input().split())
board = []

for i in range(N):
    board.append(input())

ans = solve(N, M, board)
ans = ans%1000000007
print(ans)

