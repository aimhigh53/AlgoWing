def solution(dp):
    global array
    n = len(array)
    init_dp(dp)
    for x in range(1,n) :
        for y in range(1,n):
            dp[x][y] = min(dp[x-1][y], dp[x][y-1]) + array[x][y]

def init_dp(dp):
    global array
    dp[0][0] = array[0][0]
    n = len(array)
    for i in range(1,n):
        dp[0][i] = dp[0][i-1] + array[0][i]
        dp[i][0] = dp[i-1][0] + array[i][0]

T = int(input())
testCases = []
for i in range(T):
    temp = []
    n = int(input())
    for i in range(n):
        temp.append(list(map(int,input().split())))
    testCases.append(temp)

for idx, array in enumerate(testCases):
    n = len(array)
    dp = [[float('inf') for k in range(n)] for j in range(n)]
    solution(dp)
    print("#" + str(idx+1) +" " + str(dp[n-1][n-1]))

