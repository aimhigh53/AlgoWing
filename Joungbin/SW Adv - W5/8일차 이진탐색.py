t=int(input())

def inorder(x) :
    global order
    if(x==-1) :
        return
    inorder(child_node[x][0])
    order.append(x)
    inorder(child_node[x][1])

for tc in range(t) :
    n = int(input())
    child_node = [[-1] * 2 for _ in range(n + 1)]
    order = [0]
    for i in range(1, n//2+1) :
        if(2*i<=n) :
            child_node[i][0] = 2 * i
        if(2*i+1<=n) :
            child_node[i][1] = 2 * i + 1
    inorder(1)
    print(order, child_node)
    print('#%d'%(tc+1), order.index(1), order.index(n//2))