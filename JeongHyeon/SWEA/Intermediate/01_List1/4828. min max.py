## 4828. min max
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

T = int(input())
for test_case in range(1, T + 1):
    length = int(input())
    L = list(map(int, input().split()))
    print('#' + str(test_case), max(L)-min(L))