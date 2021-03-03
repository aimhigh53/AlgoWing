n, m = map(int, input().split())
mem = [*map(int, input().split())]
cost = [*map(int, input().split())]
k = 10001
d = [[0] * k for _ in range(n + 1)]
# d[i][j]는 i번째까지의 비용이 j일 때, 최대 메모리 확보량
ans = 0

for i in range(n):
    x, c = mem[i], cost[i]
    for j in range(k):
        if (j >= c): # 총 비용이 현재 비용보다 크거나 같은 경우
            d[i + 1][j] = max(d[i][j - c] + x, d[i][j])
            # 총 비용에서 현재 비용을 뺄 수 있으므로 둘 중에 더 큰 값 저장
        else: # 아닌 경우
            d[i + 1][j] = d[i][j] # 경우의 수는 1가지

for i in range(k):
    if (d[-1][i] >= m): ans = i; break # 최소 비용 찾기

print(ans)
