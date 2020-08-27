import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

from collections import deque

# dfs 활용
def dfs(start):
    # 최종 return 할 값, 처음엔 무한대로 설정
    min_recharge = float('inf')
    recharge = 0
    stack = deque()
    # stack에 정류장 숫자와 그 정류장에 도달했을때 충전횟수 같이 저장
    stack.append((start, recharge))
    while stack:
        tmp = stack.pop()
        curr_stop = tmp[0]
        curr_recharge = tmp[1]
        move = data[curr_stop]
        # 현재 충전횟수가 현재 min_recharge 보다 크면 건너뛴다
        if curr_recharge > min_recharge:
            continue

        # min_recharge 보다 작으면 다음 정류장을 stack에 넣어준다
        else:
            for i in range(1, move+1):
                next_stop = curr_stop + i
                # 목적지 이상을 도착하면 충전횟수를 확인하고 업데이트 해준다
                if next_stop >= N:
                    min_recharge = min(min_recharge, curr_recharge)
                else:
                    stack.append((next_stop, curr_recharge + 1))
        # print(stack)
    return min_recharge

T = int(input())
for test_case in range(1, T + 1):
    data = list(map(int, input().split()))
    N = data[0]

    print('#{} {}'.format(test_case, dfs(1)))

'''
test case2 예시
#2 2
deque([(2, 1), (3, 1)])
deque([(2, 1), (4, 2), (5, 2), (6, 2)])
deque([(2, 1), (4, 2), (5, 2), (7, 3), (8, 3), (9, 3)])
deque([(2, 1), (4, 2), (6, 3), (7, 3)])
deque([(2, 1), (5, 3), (6, 3)])
deque([(3, 2)])
deque([(4, 3), (5, 3), (6, 3)])
'''
