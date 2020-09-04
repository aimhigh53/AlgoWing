## 4836_색칠하기
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    red_area = []
    blue_area = []
    for _ in range(N) :
        x1, y1, x2, y2, color = map(int, input().split())
        for x in range(x1, x2+1) :
            for y in range(y1, y2+1) :
                if color == 1 :
                    if (x, y) not in red_area :
                        red_area.append((x, y))
                else :
                    if (x, y) not in blue_area :
                        blue_area.append((x, y))

    # 같은 위치 비교
    answer = 0
    for red in red_area :
        for blue in blue_area :
            if red == blue :
              answer += 1

    print('#' + str(test_case), answer)