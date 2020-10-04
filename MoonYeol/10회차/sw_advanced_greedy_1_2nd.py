import heapq

def getMinus(n):
    return int(n) * -1

def solution(freight,truck):
    answer = 0
    next =True
    i = 0
    j = 0
    while truck and freight:
        if next:
            i = heapq.heappop(truck) * -1
            j = heapq.heappop(freight) * -1
            next = False
        else:
            j = heapq.heappop(freight) * -1
        if i >= j:
            answer += j
            next = True
    return answer


nums = int(input())
freights = []
trucks = []
for i in range(nums):
    n,m = map(int,input().split())
    freight = list(map(getMinus, input().split()))
    truck = list(map(getMinus,input().split()))
    heapq.heapify(freight)
    heapq.heapify(truck)
    freights.append(freight)
    trucks.append(truck)

for i in range(nums):
    answer = solution(freights[i],trucks[i])
    print("#" + str(i+1) +" " + str(answer))
