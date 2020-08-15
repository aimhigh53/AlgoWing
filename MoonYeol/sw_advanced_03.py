def solution(array, i, j):
    if i + 1 == len(array) and j + 1 == len(array[i]):
        return array[i][j]
    if  i + 1 < len(array) and j + 1 < len(array[i]):
        return array[i][j] + min(solution(array, i+1,j),solution(array, i, j + 1))
    if i + 1 < len(array):
        return array[i][j] + solution(array, i + 1 , j)
    if j + 1 < len(array[i]):
        return array[i][j] + solution(array, i , j + 1)


num = int(input())
nums = []
for i in range(num):
    temp = []
    n = int(input())
    for i in range(n):
        temp.append(list(map(int,input().split())))
    nums.append(temp)

for i,j in enumerate(nums):
    answer = solution(j,0,0)
    print("#" + str(i+1) +" " + str(answer))

