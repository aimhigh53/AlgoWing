## 5253_접두어 검색
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

T = int(input())
for test_case in range(1, T + 1):
    Text_len, prefix_len = map(int, input().split())

    Text_list = []
    for _ in range(Text_len) :
        Text_list.append(input())

    prefix_list = []
    for _ in range(prefix_len) :
        prefix_list.append(input())

    answer = 0
    for prefix in prefix_list :
        for text in Text_list :
            if prefix == text[0:len(prefix)] :
                answer += 1
                break
    print('#' + str(test_case), answer)