# 출처: https://inspirit941.tistory.com/134
# dp 로 풀지만 시간복잡도 n^2 인 풀이

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

n = int(input())
my_lst = list(map(int, input().split()))
dp = [1 for _ in range(n)]
# print(n, my_lst)

for i in range(n):
    for j in range(i):
        if my_lst[i] > my_lst[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

     