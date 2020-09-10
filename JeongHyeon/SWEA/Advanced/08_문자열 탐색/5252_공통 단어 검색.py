## 5252_공통 단어 검색
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

T = int(input())
for test_case in range(1, T + 1):
    A_len, B_len = map(int, input().split())

    A_list = []
    for _ in range(A_len) :
        A_list.append(input())

    B_list = []
    for _ in range(B_len) :
        B_list.append(input())

    answer = 0
    for a in A_list :
        for b in B_list :
            if a == b :
                answer += 1

    print('#' + str(test_case), answer)