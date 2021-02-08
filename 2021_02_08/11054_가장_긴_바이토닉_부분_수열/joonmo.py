# 가장 긴 증가하는 부분수열 풀이를 2번 실행한다. 
# 한번은 수열을 뒤집어서 가장 긴 감소하는 부분수열 구한다.


import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

N = int(input())
my_lst = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if my_lst[i] > my_lst[j]:
            dp[i] = max(dp[i], dp[j]+1)
# print(my_lst)
# print(dp)

my_lst = my_lst[::-1]
dp2 = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if my_lst[i] > my_lst[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

# print(my_lst)
# print(dp2)

dp3 = []

for i in range(N):
    dp3.append(dp[i] + dp2[N-i-1])

print(max(dp3)-1)
