#dfs bfs의 정
n=int(input())
edge_num=int(input())
computers=[]
for _ in range(edge_num):
    a,b=map(int,input().split())
    computers.append([a,석b])
    computers.append([b,a])

computers.sort(key= lambda x:x[0])

stack=[1]
visited=[0 for _ in range(n+1)]
while(stack):
    now=stack.pop()
    visited[now]=1
    for computer in computers:
        if computer[0]==now and visited[computer[1]]==0:
            stack.append(computer[1])
print(visited.count(1)-1)