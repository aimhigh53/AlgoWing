## 4839_ 이진탐색
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

def binary_search(first_page, last_page, find_page, count) :
    center_page = int((first_page + last_page) / 2)
    if find_page == center_page :
        return count
    else :
        count += 1
        if find_page < center_page :
            last_page = center_page
            return binary_search(first_page, last_page, find_page, count)
        else :
            first_page = center_page
            return binary_search(first_page, last_page, find_page, count)

T = int(input())
for test_case in range(1, T + 1):
    last_page, A, B = map(int, input().split())
    A_count = binary_search(1, last_page, A, 0)
    B_count = binary_search(1, last_page, B, 0)
    if A_count == B_count :
        answer = 0
    elif A_count < B_count :
        answer = 'A'
    else :
        answer = 'B'
    print('#' + str(test_case), answer)