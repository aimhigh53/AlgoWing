t=int(input())

def dfs(x) :
    global count
    ch[x]=1
    for i in connected_node[x] :
        if(ch[i]==0) :
            count+=1
            dfs(i)

for tc in range(t) :
    e, n = map(int, input().split())
    input_list = list(map(int, input().split()))
    m = max(input_list)
    connected_node=[[] for _ in range(m + 1)]
    count=1
    for edge in range(e) :
        vertex1, vertex2 = input_list[2 * edge], input_list[2 * edge + 1]
        connected_node[vertex1].append(vertex2)
    ch=[0]*(m+1)
    dfs(n)
    print('#%d' % (tc+1), count)