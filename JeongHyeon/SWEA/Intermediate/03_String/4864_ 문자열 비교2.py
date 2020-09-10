## 4864_ 문자열 비교
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
# 보이어-무어 알고리즘
# 테스트케이스 10개중 2개 틀림

def compare (find_len, find_str, long_str) :
    success = 0
    for i in range(find_len-1, -1, -1) :
        if find_str[i] == long_str[i] :
            success += 1
        elif long_str[i] in find_str :
            return list(reversed(find_str)).index(long_str[i]) # reversed(find_str) > object반환
        elif long_str[i] not in find_str :
            return 0
    return success

T = int(input())
for test_case in range(1, T + 1):
    find_str = list(input())
    long_str = list(input())
    find_len = len(find_str)
    long_len = len(long_str)

    # score_list = [i for i in range(find_len-1, -1, -1)]
    # find_str_score = dict(zip(find_str, score_list))
    # > find_str에 중복문자 있을 경우 문제

    idx = 0
    continue_True = True
    while continue_True :
        compare_answer = compare(find_len, find_str, long_str[idx : idx + find_len])
        if compare_answer == find_len :
            answer = 1
            continue_True = False
        elif compare_answer == 0 :
            idx += find_len
        elif compare_answer < find_len :
            idx += compare_answer
        if (idx + find_len) > long_len :
            answer = 0
            continue_True = False

    print('#' + str(test_case), answer)