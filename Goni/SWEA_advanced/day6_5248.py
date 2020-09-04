#와 진짜진짜 노가다고 통과한게 신기함

import sys

sys.stdin = open("sample_input.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    num, M = map(int, input().split())
    temp = list(map(int, input().split()))
    pairs = []
    for i in range(0, 2 * M, 2):
        pairs.append({temp[i], temp[i + 1]})

    dict_ans = dict.fromkeys([i for i in range(1, num + 1)])

    for check in range(1, num + 1):
        for each in pairs:
            if check in each and min(each) == check:
                if dict_ans[check]:
                    temp = each | dict_ans[check]
                else:
                    temp = each
                dict_ans[check] = temp
    nogada = 0
    while (nogada!=5):
        for i in range(1, len(dict_ans) + 1):
            for k in range(i + 1, len(dict_ans) + 1):
                if dict_ans[i] and dict_ans[k]:
                    temp = dict_ans[i] & dict_ans[k]
                    if len(temp) > 0:
                        dict_ans[i] = dict_ans[i] | dict_ans[k]
                        dict_ans[k] = None
        nogada+=1

    temp = {0}
    ans = 0

    for i in dict_ans.values():
        if i:
            temp = temp | i
            ans += 1

    for i in range(1, num + 1):
        if i not in temp:
            ans += 1

    print("#{} {}".format(test_case, ans))
