import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')


def grid_print(grid):
    for i in grid:
        print(i)

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(map(int,input().split())))
    # grid_print(grid)

    dp = [[0 for _ in range(N)] for _ in range(N)]
    
    dp[0][0] = grid[0][0]
    
    for y in range(N):
        for x in range(N):
            if x == 0 and y==0:
                continue
            elif x == 0:
                dp[y][x] = grid[y][x] + dp[y-1][x]
            elif y == 0:
                dp[y][x] = grid[y][x] + dp[y][x-1]
            else:
                dp[y][x] = grid[y][x] + min(dp[y-1][x], dp[y][x-1])
    # print()
    # grid_print(dp)

    print('#{} {}'.format(test_case, dp[N-1][N-1]))