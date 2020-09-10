## 5254_부분 문자열
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
# 테케 10개 중 1개 틀림 & 런타임 에러

T = int(input())
for test_case in range(1, T + 1):
    number, text = input().split()
    number = int(number)

    partStr_list = []
    for i in range(len(text)) :
        for j in range(len(text)) :
            if j >= i and (j+1) <= len(text):
                partStr_list.append(text[i:j+1])
    partStr_list = sorted(list(set(partStr_list)))
    # print(partStr_list)
    answer = partStr_list[number-1]
    print('#' + str(test_case), answer[0], len(answer))