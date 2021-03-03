N = int(input())
weight = list(map(int,input().split()))
weight.sort()
num = 1
for i in range(N):
    if num < weight[i]:
        break
    num += weight[i]
print(num)
