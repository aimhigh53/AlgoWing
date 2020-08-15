def solution(array, x, y,visited):
    if visited +1 == 1 << (len(array) +1) :
        return array[x][y] + array[y][0]
    temp = []
    for i,j in enumerate(array[x]):
        if not (visited & 1<<i):
            temp.append(array[x][y] +solution(array, y, i, visited | 1<< i))

    return min(temp)

num = int(input())
nums = []
visited = []
for i in range(num):
    temp = []
    n = int(input())
    temp2 = (1 << n) | 1
    for i in range(n):
        temp.append(list(map(int,input().split())))
    nums.append(temp)
    visited.append(temp2)

for i,j in enumerate(nums):
    answer = solution(j,0,0,visited[i])
    print("#" + str(i+1) +" " + str(answer))

