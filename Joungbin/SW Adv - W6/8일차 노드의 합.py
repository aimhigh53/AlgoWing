t = int(input())

for tc in range(t):
    n, m, l = map(int, input().split()) # 리프 노드의 개수 m=(n+1)//2
    a = [0]*(n+1)
    for leaf_node in range(m):
        node_num, node_value = map(int, input().split())
        a[node_num] = node_value
    for parent_node in range(n // 2, 0, -1):
        if(2 * parent_node + 1 <= n):
            a[parent_node] = a[2 * parent_node] + a[2 * parent_node + 1]
        else:
            a[parent_node] = a[2 * parent_node]
    print('#%d' %(tc+1), a[l])
