import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def graph_print(graph):
    for i in graph:
        print(i)

def inBound(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    else:
        return False


test_case = int(input())
for t in range(test_case):
    N = int(input())
    
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    # graph_print(graph)
    
        INF = float('inf')
    distance = [[INF for _ in range(N)] for _ in range(N)]
    distance[0][0] = 0

    q = deque()
    q.append((0,0))
    while q:
        curr_y, curr_x = q.popleft()
        for i in range(4):
            tmp_x = curr_x + dx[i] 
            tmp_y = curr_y + dy[i]
            if inBound(tmp_x, tmp_y):
                tmp_gas = 1
                if graph[tmp_y][tmp_x] > graph[curr_y][curr_x]:
                    tmp_gas += graph[tmp_y][tmp_x] - graph[curr_y][curr_x]
                if distance[tmp_y][tmp_x] > distance[curr_y][curr_x] + tmp_gas:
                    distance[tmp_y][tmp_x] = distance[curr_y][curr_x] + tmp_gas
                    q.append((tmp_y, tmp_x))
    # graph_print(distance)

    print('#{} {}'.format(t+1, distance[N-1][N-1]))