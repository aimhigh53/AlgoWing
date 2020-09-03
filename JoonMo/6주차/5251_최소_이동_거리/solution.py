# https://mungto.tistory.com/249 참고

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

import heapq

test_case = int(input())
for t in range(test_case):
    N, E = map(int, input().split())
    distance =[0] + [float('inf') for _ in range(N)]
    node = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]

    for _ in range(E):
        s, e, w = list(map(int, input().split()))
        node[s].append((e, w))

    queue = []
    heapq.heappush(queue, (0, 0))

    while queue:
        d, idx = heapq.heappop(queue)
        for a, b in node[idx]:
            if distance[a] > d + b:
                    distance[a] = d + b
                    heapq.heappush(queue, (distance[a], a))


    print('#{} {}'.format(t+1, distance[N]))