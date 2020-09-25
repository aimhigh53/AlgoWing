from itertools import permutations

t = int(input())

for tc in range(t):
    n = int(input())
    cart_cost = []
    ans = 0
    for i in range(n):
        cart_cost.append(list(map(int, input().split())))
    numlist = [*range(1, n)]
    permu_list = list(permutations(numlist, n - 1))
    for i in range(len(permu_list)):
        s = 0
        s += cart_cost[0][permu_list[i][0]]
        for j in range(1, n-1):
            s += cart_cost[permu_list[i][j - 1]][permu_list[i][j]]
        s += cart_cost[permu_list[i][n - 2]][0]
        if(ans == 0 or s < ans):
            ans = s
    print(ans)
