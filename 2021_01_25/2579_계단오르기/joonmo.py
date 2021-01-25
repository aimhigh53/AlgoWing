# 틀림

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

N = int(input())
arr = []
dp = []

for _ in range(N):
    arr.append(int(input()))

dp.append(arr[0])
dp.append(arr[0]+ arr[1])
dp.append(max(arr[0]+arr[2], arr[1]+arr[2]))

for i in range(3, N):
    dp.append(max(dp[i-3] + arr[i-1] + arr[i], dp[i-1] + arr[i]))

print(dp)
print(dp[-1])



