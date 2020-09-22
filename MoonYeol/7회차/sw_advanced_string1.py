T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    tempA =set()
    ans = 0
    for j in range(N):
        tempA.add(input())
    for j in range(M):
        B =input()
        if B in tempA:
            ans +=1
    print("#" +str(i+1) + " " +str(ans))