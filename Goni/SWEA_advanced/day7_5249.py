import sys
sys.stdin=open("sample_input.txt",'r')
def renewal_key(next,now_weight):
    if visited[next] == False and now_weight <= key[next]:
        key[next] = now_weight
        parent_node[next] = minIndex

T=int(input())

for test_case in range(1,T+1):
    node_num,edge_num=map(int,input().split())
    graph=[]
    for _ in range(edge_num):
        start,end,weight=map(int,input().split())
        graph.append([(start,end),weight])

    key=[float('inf')]*(node_num+1)
    parent_node=[None]*(node_num+1)
    visited=[False]*(node_num+1)
    key[0]=0
    tree=[]


    for _ in range(node_num):
        minIndex=-1
        minimum=float('inf')
        for i in range(node_num+1):
            if visited[i]==False and key[i]<=minimum:
                minimum=key[i]
                minIndex=i
        visited[minIndex]=True

        for node in graph:
            if minIndex == node[0][0]:
                next=node[0][1]
                now_weight = node[1]
                renewal_key(next,now_weight)
            elif minIndex ==node[0][1]:
                next=node[0][0]
                now_weight = node[1]
                renewal_key(next,now_weight)

    print("#{} {}".format(test_case,sum(key)))
