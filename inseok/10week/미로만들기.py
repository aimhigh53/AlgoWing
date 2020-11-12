from collections import deque

N=int(input())
field=[0]*N

visited=[[-1]*N for _ in range(N)]
##str.... 분기문 쓸때 주의해야함!


for i in range(N):
    tmp=input()
    field[i]=list(tmp)

#얘도 bfs
#상하좌우는 무조건,,
#근데 여기에 뭔가 하나가 더 있는느낌

#후보군-->더 이상 길을 갈 수 없는 지역일 때,,,
#다 돌고나서 최솟값인 길이 그 길이면됨

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(N,field,visited):

    q=deque()
    q.append((0,0))
    visited[0][0]=0
    while q:
        element=q.pop()
        i,j=element[0],element[1]

        if i==N-1 and j==N-1:
            print(visited[i][j])
            return

        for d in range(4):
            my,mx=i+dy[d],j+dx[d]
            if my<0 or mx<0 or my>=N or mx>=N:
                continue

            if visited[my][mx]==-1:
                if field[my][mx]=='1':
                    visited[my][mx]=visited[i][j]
                    q.append((my,mx))
                else:
                    visited[my][mx]=visited[i][j]+1
                    q.appendleft((my,mx))


            #3면이 막혀있는것을 알아내서, 색을 전환한다, 전환되는 곳은 길이 더 나아갈 수 있냐 없냐..

def solution(N,field):
    bfs(N,field,visited)


solution(N,field)


## 문제가 됐던거
#1. str->int 비교하는데 비교가 당연히 안되지,,,
#2. 알아서 찾아가는데 굳이 더 생각할 필요가 없었다.

