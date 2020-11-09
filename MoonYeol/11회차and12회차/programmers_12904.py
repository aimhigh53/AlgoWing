

def solution(s):
    answer = 1
    len_s = len(s)
    dp = [[-1 for _ in range(len_s)] for _ in range(len_s)]
    for i in range(len_s):
        dp[i][i] = 1
    for i in range(len_s-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 1
            answer = 2
    for k in range(3,len_s+1):
        for a in range(len_s-k+1):
            b = a+k -1
            if s[a] == s[b] and dp[a+1][b-1] == 1:
                dp[a][b] = 1
                answer = max(answer,b-a+1)
                
    
    return answer