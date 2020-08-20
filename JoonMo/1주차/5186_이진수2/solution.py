import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

T = int(input())
for test_case in range(1,T+1):
    answer = ''
    N = float(input())
    num = 1
    for _ in range(12):
        num /= 2
        if N - num >= 0:
            answer += '1'
            N -= num
            if not N:
                break
        else:
            answer += '0'

    if N:
        answer = 'overflow'
    print('#{} {}'.format(test_case, answer))