import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

from itertools import permutations

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

    route = [ i for i in range(2,N+1)]
    route_perm = list(permutations(route))
    # print(route_perm)

    answer = float('inf')
    for i in route_perm:
        tmp_min = grid[0][i[0]-1]
        # print(i)
        for idx in range(N-1):
            # print(idx)
            if idx+1 < N-1:
                tmp_min += grid[i[idx]-1][i[idx + 1]-1]
                # print(tmp_min)
        tmp_min += grid[i[-1]-1][0]
        # print(tmp_min)
        if tmp_min < answer:
            answer = tmp_min
    
    print('#{} {}'.format(test_case, answer))