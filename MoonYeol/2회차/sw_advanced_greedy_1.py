def solution(freight,truck):
    answer = 0
    temp = 0
    is_break = False
    freight.sort(reverse=True)
    truck.sort(reverse=True)
    for i in truck:
        for j in freight:
            if i >= j :
                answer += j
                temp = j
                is_break =True
                break
        if is_break :
            freight.remove(temp)
            is_break=False
    return answer


nums = int(input())
freights = []
trucks = []
for i in range(nums):
    n,m = map(int,input().split())
    freights.append(list(map(int, input().split())))
    trucks.append(list(map(int,input().split())))


for i in range(nums):
    answer = solution(freights[i],trucks[i])
    print("#" + str(i+1) +" " + str(answer))
