## 4861_ 회문
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
# 세로줄 리스트 만드는거 왜안돼애아아ㅣ아아아ㅏㄱ

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    sentence_array = []
    for _ in range(N) :
        sentence_array.append(list(input()))

    # 가로줄 확인
    for sentence in sentence_array :
        for i in range(len(sentence)-M+1) :
            check_str = sentence[i:M+1]
            if check_str == check_str[::-1] :
                answer = check_str

    # 세로줄 확인
    Sero_sentence_array = [[0] * N ] * N
    for first in range(N) :
        sentence = sentence_array[first]
        for second in range(N) :
            Sero_sentence_array[second][first] = sentence[second]

    print(Sero_sentence_array)
    # print('#' + str(test_case), answer)

