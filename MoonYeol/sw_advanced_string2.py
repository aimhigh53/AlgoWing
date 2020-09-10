def solution(Alist, Blist):
    ans = 0
    for j in Blist:
        for i in Alist:
            if len(i)<len(j):
                continue
            else:
                temp = i[:len(j)]
                if j == temp:
                    ans +=1
                    break
    return ans

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    Alist = []
    Blist = []
    for j in range(N):
        Alist.append(input())
    for j in range(M):
        Blist.append(input())
    answer = solution(Alist, Blist)
    print("#" +str(i+1) + " " +str(answer))