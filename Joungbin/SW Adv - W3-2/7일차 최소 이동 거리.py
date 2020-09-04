t = int(input())

for tc in range(t):
    n, e = map(int, input().split()) # n : 정점 번호 중 가장 큰 수, e : 간선의 개수
    check = [0] * (n + 1)
    node_info = [[] for _ in range(n + 1)]
    inf = 10**9
    dist = [-1]*(n+1)
    for i in range(1, n+1):
        dist[i] = inf
    dist[0] = 0

    for vertex in range(e):
        start_node, end_node, vertex_cost=map(int, input().split())
        node_info[start_node].append((end_node, vertex_cost))

    for check_node in range(n):
        m = inf+1
        start_node = -1
        for i in range(n+1): # 다음 정점을 고르는 과정
            if(check[i] == 0 and m > dist[i]):
                m = dist[i]
                start_node = i
            check[start_node] = 1
        for choose_vertex in range(len(node_info[start_node])):
            end_node = node_info[start_node][choose_vertex][0]
            if(dist[end_node] > dist[start_node] + node_info[start_node][choose_vertex][1]):
                dist[end_node] = dist[start_node] + node_info[start_node][choose_vertex][1]

    print('#%d'%(tc+1), dist[n])