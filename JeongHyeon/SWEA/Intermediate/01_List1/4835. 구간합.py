## 4835. 구간합
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    sum_case = []
    for i in range(N - M + 1) :
        sum = 0
        for m in range(M) :
            sum += numbers[i + m]
        sum_case.append(sum)

    print('#' + str(test_case), max(sum_case)-min(sum_case))