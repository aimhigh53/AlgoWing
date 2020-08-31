from collections import deque

answer = 0
num = int(input())
numbers = []
for i in range(num):
    numbers.append(list(map(int, input().split())))

for idx, i in enumerate(numbers):

    N,M = i
    q = deque()
    q.append([N,0])
    visited = [False for i in range(1000001)]
    while True:
        n,count = q.popleft()
        if 0 >= n  or n > 1000000:
            continue
        if visited[n]:
            continue
        else:
            visited[n] = True
        if n == M:
            answer = count
            break
        q.append([n + 1,count+1])
        q.append([n-10,count+1])
        q.append([n-1,count+1])
        q.append([n*2,count+1])

    print("#" + str(idx+1) +" " + str(answer))

