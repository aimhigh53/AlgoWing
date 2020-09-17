import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

T = int(input())
for test_case in range(1,T+1):
    answer = ''
    N = float(input())
    num = 1
    cnt = 0
    while True:
        num /= 2
        if N >= num:
            N -= num
            answer += '1'
        else:
            answer += '0'
        
        # print(num)
        cnt += 1

        if N == 0:
            break

        if cnt >=13:
            answer = 'overflow'
            break  
    

    print('#{} {}'.format(test_case, answer))