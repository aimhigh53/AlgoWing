from collections import deque

t = int(input())

for tc in range(t):
    v, e = map(int, input().split()) # v : 정점 번호 중 가장 큰 수, e : 간선의 개수
    check = [0] * (v + 1)
    node_info = [[] for _ in range(v + 1)]
    answer = 0

    for vertex in range(e):
        start_node, end_node, vertex_cost = map(int, input().split())
        node_info[start_node].append((end_node, vertex_cost))
        node_info[end_node].append((start_node, vertex_cost))

    q = deque()
    check[0] = 1 # 0부터 시작
    for vertex_info in node_info[0]:
        q.append(vertex_info)

    while q:
        next_node, vertex_cost = q.popleft()
        if(check[next_node] == 1):
            continue
        for i in range(len(q)): # 큐에 들어있는 모든 순서쌍 중 다음으로 방문할 곳을 찾는 과정
            x2, y2 = q.popleft()
            if(check[x2] == 1):
                continue
            elif(y2 >= vertex_cost):
                q.append((x2, y2))
                continue
            else:
                q.append((next_node, vertex_cost))
                next_node, vertex_cost = x2, y2
        answer += vertex_cost
        check[next_node] = 1
        for vertex_info in node_info[next_node]:
            q.append(vertex_info)
        if(check.count(0) == 0) : # 0부터 v까지 모두 방문한 경우 종료
            break
    print('#%d' % (tc+1), answer)