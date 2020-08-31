# https://mungto.tistory.com/221 참고했습니다

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

def get_parent(n):
    if parent[n] != n:
        parent[n] = get_parent(parent[n])
    return parent[n]

def union(x, y):
    a = get_parent(x)
    b = get_parent(y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for t in range(int(input())):
    N,M = map(int, input().split())
    parent = [i for i in range(N+1)]
    votes = list(map(int, input().split()))

    for i in range(0, M*2, 2): 
        union(votes[i], votes[i+1])

    answer = set()
    for i in parent: 
        answer.add(get_parent(i))
    # print(parent, answer)

    print('#{} {}'.format(t+1, len(answer)-1))