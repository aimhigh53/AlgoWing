Testcase=int(input())
 
##dfs는 최단 경로일때 모두를 다 찾지만,BFS는 모든 경로를 다 찾지않고 최소를 찾으면 종료해버림
 
mX=[0,1]
mY=[1,0]
 
#그래서 그냥 dfs로 풀어내자
def sol(i,j):
    global field
    global table
 
    if i==N-1 and j==N-1:
        return 
 
    for k in range(2):
        dx,dy=i+mX[k],j+mY[k]
        if dx<N and dy<N:
            if table[dx][dy]==0:
                table[dx][dy]=table[i][j]+field[dx][dy]
            else:
                if table[dx][dy]>table[i][j]+field[dx][dy]:
                    table[dx][dy]=table[i][j]+field[dx][dy]
 
 
            sol(dx,dy)
 
 
 
for tc in range(1,1+Testcase):
    N=int(input())
    field=[0]*N
    table=[[0]*N for _ in range(N)]
 
    for i in range(N):
        field[i]=list(map(int,input().split(' ')))
 
    table[0][0]=field[0][0]
    sol(0,0)
 
    print("#{} {}".format(tc,table[N-1][N-1]))
 
