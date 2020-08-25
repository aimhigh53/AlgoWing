def solution(freight,time):
    count = 0
    sort_fre = sorted(freight, key= lambda x : x[1])
    for i in sort_fre:
        if time <= i[0]:
            time = i[1]
            count +=1
    return count


nums = int(input())
freights = []
for i in range(nums):
    n = int(input())
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
    freights.append(temp)

for idx, i in enumerate(freights):
    answer = solution(i,0)
    print("#" + str(idx+1) +" " + str(answer))
