def solution(N,numbers,y,count,visited):
    global answer
    if count > answer:
        return
    if y >= N:
        answer = count
        return

    for i in range(N):
        if not (visited & 1<<i) :
            solution(N,numbers,y+1,count+numbers[i][y], visited | 1<<i)
    return


num = int(input())
numbers = []
Ns = []
for i in range(num):
    N = int(input())
    Ns.append(N)
    temp = []
    for j in range(N):
        temp.append(list(map(int, input().split())))
    numbers.append(temp)

for idx, i in enumerate(numbers):
    answer = float('inf')
    solution(Ns[idx], i, 0, 0, 1<<Ns[idx])
    print("#" + str(idx+1) +" " + str(answer))