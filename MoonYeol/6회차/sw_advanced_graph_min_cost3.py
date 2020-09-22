
def dijkstra(N, E, graph):
    INF = float('inf')
    s = [False] * E
    d = [INF] * E
    d[0] = 0

    while True:
        m = INF
        Node = -1
        for k in range(E):
            if s[k]: continue
            if m > d[k]:
                m = d[k]
                Node = k
        if m == INF:
            break
        s[Node] = True
        for k in range(E):
            if s[k]: continue
            via = d[Node] + graph[Node][k]
            if d[k] > via:
                d[k] = via
    return d[N]


num = int(input())
testCases = []
Ns = []
Es = []
for i in range(num):
    temp = []
    N, E = map(int, input().split())
    Ns.append(N)
    Es.append(E)
    for j in range(E):
        temp.append(list(map(int, input().split())))
    testCases.append(temp)

for idx, i in enumerate(testCases):
    INF = float('inf')
    N, E = Ns[idx], Es[idx]
    graph = [[INF for k in range(E)] for j in range(E)]
    for j in i:
        u, v, w = j
        graph[u][v] = w
    print("#" + str(idx + 1) + " " + str(dijkstra(N, E, graph)))
