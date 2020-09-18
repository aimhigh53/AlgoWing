def solution(N,numbers,idx,count):
    global answer
    if count > answer:
        return
    if idx >= N:
        answer = count
        return
    battery = numbers[idx]
    for i in range(battery,0,-1):
        solution(N,numbers,idx+i,count+1)
    return


num = int(input())
numbers = []
Ns = []
for i in range(num):
    temp = list(map(int, input().split()))
    Ns.append(temp.pop(0))
    numbers.append(temp)

for idx, i in enumerate(numbers):
    answer = float('inf')
    solution(Ns[idx]-1,i,0,-1)
    print("#" + str(idx+1) +" " + str(answer))