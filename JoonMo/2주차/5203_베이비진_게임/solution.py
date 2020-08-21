
import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

def check_run(lst):
    temp = 0
    for i in lst:
        if i != 0:
            temp += 1
            if temp >= 3:
                return True
        else:
            temp = 0
    return False
    # for i in range(len(lst)):
    #     if i+2 <= len(lst):
    #         if lst[i] > 0 and lst[i+1] > 0 and lst[i+2] > 0:
    #             return True
    # return False

def check_triplet(lst):
    if 3 in lst:
        return True
    return False

def check_win(lst):
    if check_run(lst) or check_triplet(lst):
        return True
    return False

T = int(input())
for test_case in range(1, T + 1):
    cards = list(map(int, input().split()))
    # print(cards)
    player1 = [0 for _ in range(10)]
    player2 = [0 for _ in range(10)]

    answer = 0
    for i in range(6):
        tmp1 = cards[2*i]
        player1[tmp1] += 1
        tmp2 = cards[2*i +1]
        player2[tmp2] += 1
        # print(player1, player2)

        if i>=2:
            if check_win(player1):
                answer = 1
                break
            elif check_win(player2):
                answer = 2
                break

    print('#{} {}'.format(test_case, answer))
