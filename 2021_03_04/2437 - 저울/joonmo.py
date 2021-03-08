# 출처:https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%802437%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%A0%80%EC%9A%B8

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

N = int(input())
weight = list(map(int, input().split()))

weight.sort()
# print(N, weight)

tmp_sum = 0

for i in range(N):
    if tmp_sum + 1 >= weight[i]:
        tmp_sum += weight[i]
    else:
        break

print(tmp_sum + 1)