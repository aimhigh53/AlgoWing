# https://mungto.tistory.com/247 를 참고했습니다.

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

from collections import deque

def bfs(N, M):
    q = deque()
    q.append((N, 0))
    check = {}
    while q:
        num, cnt = q.popleft()
        if check.get(num, 0):
            continue
        check[num] = 1
        if num == M:
            return cnt
        cnt += 1
        if 0 < num + 1 <= 1000000:
            q.append((num + 1, cnt))
        if 0 < num - 1 <= 1000000:
            q.append((num - 1, cnt))
        if 0 < num * 2 <= 1000000:
            q.append((num * 2, cnt))
        if 0 < num - 10 <= 1000000:
            q.append((num - 10, cnt)) 

for t in range(int(input())):
    N,M = map(int, input().split())
    print('#{} {}'.format(t+1, bfs(N,M)))