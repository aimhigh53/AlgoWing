# 출처:https://chancoding.tistory.com/60
# bfs dfs로 아무거나 풀어도 나오는 문제

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

from collections import deque

a = int(input())
b = int(input())
my_dict = dict()
for i in range(a):
    my_dict[i+1] = set()

for _ in range(b):
    fir, sec = map(int, input().split())
    my_dict[fir].add(sec)
    my_dict[sec].add(fir)

# print(my_dict)

def dfs(start):
    visited = []
    q = deque()
    q.append(start)
    visited.append(start)

    while q:
        tmp = q.popleft()
        for i in my_dict[tmp]:
            if i in visited:
                continue
            else:
                visited.append(i)
                q.append(i)
    # print(visited)
    return(len(visited)-1)

print(dfs(1))
        
        