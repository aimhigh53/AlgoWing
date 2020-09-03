## 4837_ 부분집합의 합
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

from itertools import combinations
set_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())
for test_case in range(1, T + 1):
    N, k = map(int, input().split())
    possible_cases = list(combinations(set_A, N))
    answer = 0
    for case in possible_cases :
        if sum(case) == k :
            answer += 1

    print('#' + str(test_case), answer)