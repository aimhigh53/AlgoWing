# 참고:https://thyong.tistory.com/entry/%EB%B0%B1%EC%A4%80BOJ-15999%EB%B2%88-%EB%92%A4%EC%A7%91%EA%B8%B0-Python3

# 처음에는 직접 판을 다 눌러보면서 풀었지만 논리적으로 접근해봐야 하는 문제
# 눌러도 최종 형태에 영향을 주지 않는 칸을 찾아야한다.

# 입력 받기
N, M = map(int, input().split())
grid = [[0 for _ in range(M)] for _ in range(N)]

for n in range(N):
    grid[n] = list(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

count = 0
answer = 1

for y in range(N):
    for x in range(M):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=ny<N and 0<=nx<M:
                if grid[y][x] != grid[ny][nx]:
                    count+=1
                    break

answer = pow(2, N*M-count) % 1000000007
print(answer)