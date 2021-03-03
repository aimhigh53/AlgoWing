# dp[0][j] = dp[1][j - 1] + dp[2][j - 1] 나머지0
# dp[1][j] = dp[0][j - 1] + dp[2][j - 1] 나머지1
# dp[2][j] = dp[0][j - 1] + dp[1][j - 1] 나머지2
# j는 자리수
# 15의 배수니까, 각 자리수 더하면 3으로 나누어 떨어진다
# 1의 자리는 0또는 5
# 3으로 나누었을때 나머지가 1이면, 5를 더해주면 3으로 나눠짐
N = int(input())
result = 0
if N == 1:
    result = 0
elif N == 2:
    result = 1
else:
    dp = [[0 for _ in range(3)] for _ in range(N+1)]
    dp[1][1] = 1
    for i in range(2, N+1):
        dp[i][0] = dp[i-1][1] + dp[i-1][2]
        dp[i][1] = dp[i-1][0] + dp[i-1][2]
        dp[i][2] = dp[i-1][0] + dp[i-1][1]
        for j in range(3):
            dp[i][j] %= 1000000007
    result = dp[N][0]
result %= 1000000007
print(result)

