from collections import deque
 
testcase=int(input())
 
#웬만하면 같은 레벨에서 움직여야함
#같은 레벨, +1, 다른레벨+1+a
#4방향 모두,가중치때문에
 
#주변 다 돌아서 가중치확인,
movex=[0,1,0,-1]
movey=[1,0,-1,0]

def sol():
    q=deque()
    q.append((0,0))
    visited[0][0]=0
    while q:
        i,j=q.popleft()
        for dx,dy in zip(movex,movey):
            dx,dy=i+dx,j+dy
            if 0<=dx<N and 0<=dy<N:
                val=1
                if visited[dx][dy]<=1001 and field[i][j]<field[dx][dy]:
                    val+=(field[dx][dy]-field[i][j])
                #현재와 비교
                if visited[dx][dy]>visited[i][j]+val:
                    visited[dx][dy]=visited[i][j]+val
                    q.append((dx,dy))

 
for tc in range(1,1+testcase):
    N=int(input())
    field=[[int(x)for x in input().split(' ')]for i in range(N)]
    visited=[[1001]*N for i in range(N)]
    sol()
    print('#{} {}'.format(tc,visited[N-1][N-1]))
    

    
