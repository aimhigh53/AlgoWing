n = int(input())
k = 10**9
cost = [[*map(int, input().split())] for _ in range(n)]
d = [[k]*n for _ in range((1 << n) + 1)]
d[1][0] = 0 # 0번 도시를 시작점으로 설정

for situ in range(1, 1 << n, 2): # 어떤 도시를 방문했는지에 대한 상황(비트가 채워져 있는 경우 방문한 것으로 가정)
    for city in range(1, n): # 마지막 도시
        if(situ & (1 << city)): # 해당 도시를 방문했다면
            for prev_city in range(n): # 이전 도시 체크
                if((situ & (1 << prev_city)) and cost[prev_city][city]>0): # 이전 도시를 방문하였고 이전 도시에서 오는 길이 있는 경우
                    d[situ][city] = min(d[situ][city], d[situ - (1 << city)][prev_city] + cost[prev_city][city])
# 현재 저장되어 있는 값과 (이전 도시까지의 값 + 현재 도시로 오는 데 값)을 비교, 최솟값 저장

for i in range(n):
    if(cost[i][0] > 0):
        d[-1][i] = d[-2][i]+cost[i][0]

print(min(d[-1]))
