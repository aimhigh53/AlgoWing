import sys

sys.setrecursionlimit(10**9)

def solution(s) :
    s='0'+s
    n=len(s)
    d=[[-1]*(n) for _ in range(n)] # d[i][j] : i번째부터 j번째까지 팰린드롬을 이루는가?
                                   # 이루면 1, 아니면 0, 체크하지 않았다면 -1

    def pal(i, j) :
        if(i==j) :
            d[i][j]=1
            return 1
        elif(i+1==j) :
            if(s[i]==s[j]) :
                d[i][j]=1
                return 1
            else : return 0
        if(s[i]!=s[j]) : d[i][j]=0; return 0
        else :
            if(s[i]==s[j]) :
                d[i][j]=pal(i+1, j-1)
                return d[i][j]
        return 0

    idx=[]
    for i in range(1, n) :
        for j in range(i, n) :
            if(d[i][j]!=-1) : continue
            d[i][j]=pal(i, j)
            if(d[i][j]==1) : idx.append(j-i+1)

    answer=max(idx)
    return answer