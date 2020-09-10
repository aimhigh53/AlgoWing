## 4843_ 특별한 정렬
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    sorted_list = []
    for index in range(10) :
        if index % 2 == 0 :
            selected_num = max(num_list)
        else :
            selected_num = min(num_list)
        sorted_list.append(selected_num)
        num_list.remove(selected_num)

    answer = ''
    for num in sorted_list :
        answer += str(num)
        answer += ' '

    print('#' + str(test_case), answer)