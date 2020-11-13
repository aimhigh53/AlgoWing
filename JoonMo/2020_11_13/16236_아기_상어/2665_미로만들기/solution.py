# bfs로 풀이를 생각했지만 다익스트라 구현 연습을 위해 다익스트라 풀이 참고
# 참고: https://velog.io/@kineqwer1123/Python-%EB%B0%B1%EC%A4%80-2665

import heapq

N = int(input())
visited = [[False] * N for _ in range(N)]
maze = [list(input()) for _ in range(N)]
# print(maze)

dd = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dijkstra(start_x, start_y):
    heap_data = []
    heapq.heappush(heap_data, (0, start_x, start_y))
    visited[start_y][start_x] = True

    while True:
        cnt, now_x, now_y = heapq.heappop(heap_data)
        # print(now_x, now_y)

        # 목표지점 달성
        if now_x == N - 1 and now_y == N - 1:
            return cnt

        for x, y in dd:
            dx, dy = now_x + x, now_y + y

            # 미로 범위 확인
            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue

            if visited[dy][dx]:
                continue

            visited[dy][dx] = True

            # 검은 방일 경우 cnt +1 해주고 흰방으로 바꿔준다.
            if maze[dy][dx] == '0':
                maze[dy][dx] = '1'
                heapq.heappush(heap_data, (cnt + 1, dx, dy))
            else:
                heapq.heappush(heap_data, (cnt, dx, dy))

        # print(maze)


print(dijkstra(0, 0))



