## 02_최소합

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    size = int(input())
    grid = []

    # 0으로 이루어진 2차원 배열 생성
    # dp = [[0 for _ in range(size)] for _ in range(size)]
    dp = [[0] * size] * size

    for _ in range(size):
        grid.append(list(map(int, input().split())))
        # print(grid)

        dp[0][0] = grid[0][0]

        for y in range(size):
            for x in range(size):
                if x == 0 & y == 0:
                    continue
                elif x == 0:
                    dp[y][x] = grid[y][x] + dp[y - 1][x]