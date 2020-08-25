import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')


def binary_search(target, data):
    global cnt
    start = 0
    end = len(data) - 1
    flag = 0

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            cnt += 1
            return mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
            if flag == -1: break
            flag = -1
        else:
            end = mid -1
            if flag == 1: break
            flag = 1 

    return None

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int,input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    for i in B:
        binary_search(i,A)

    print('#{} {}'.format(test_case, cnt))