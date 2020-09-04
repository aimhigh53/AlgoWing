t = int(input())

def dfs(x):
    check[x] = 1
    for node in connected_node[x] :
        if(check[node] == 0) :
            dfs(node)

for tc in range(t):
    n, m = map(int, input().split())  # n : 사람 수, m : 종이의 장수
    input_array = list(map(int, input().split()))
    connected_node = [[] for _ in range(n + 1)]
    check = [0]*(n+1)
    answer = 0
    for vertex in range(m):
        x, y = input_array[2 * vertex], input_array[2 * vertex + 1]
        connected_node[x].append(y)
        connected_node[y].append(x)
    for node_check in range(1, n + 1):
        if(check[node_check] == 0):
            dfs(node_check)
            answer += 1
    print('#%d' % (tc+1), answer)
