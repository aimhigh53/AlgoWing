## 5247_연산
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

def operator (number, i) :
    if i == 0 :
        number += 1
    elif i == 1 :
        number -= 1
    elif i == 2 :
        number += number
    else :
        number -= 10
    return number

def repeat (N, M, count, success_num) :
    for i in range(4) :
        N = operator(N, i)
        count += 1
        if N == M :
            success_num.append(count)
        elif abs(N) < 20 : # RecursionError: maximum recursion depth exceeded in comparison
            repeat(N, M, count, success_num)
    return success_num

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    count = 0
    success_num = []
    answer = min(repeat(N, M, count, success_num))
    print('#' + str(test_case), answer)