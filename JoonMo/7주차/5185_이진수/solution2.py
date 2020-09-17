import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

hex_dict = {'0':0,'1':1, '2':2, '3':3, '4':4,'5':5,'6':6,'7':7,'8':8, '9':9,
        'A':10,'B':11,'C':12, 'D':13,'E':14,'F':15}

T = int(input())
for test_case in range(1,T+1):
    N, hex_num = map(str, input().split())
    # print(N, hex_num)

    answer = ''
    for i in hex_num:
        num = hex_dict[i]
        answer += bin(num)[2:].zfill(4)


    print('#{} {}'.format(test_case, answer))