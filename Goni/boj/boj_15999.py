#정빈님과 https://thyong.tistory.com/entry/%EB%B0%B1%EC%A4%80BOJ-15999%EB%B2%88-%EB%92%A4%EC%A7%91%EA%B8%B0-Python3

N,M = list(map(int, input().split()))
arr = [[0 for _ in range(M)] for _ in range(N)]
for n in range(N):
    arr[n] = list(input())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

count = 0
answer=1

for i in range(N) :
    for j in range(M):
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            if 0<= nx < N and 0<= ny < M :
                if arr[i][j] != arr[nx][ny] :
                    count+=1
                    break

answer = pow(2,N*M-count) % 1000000007
print(answer)