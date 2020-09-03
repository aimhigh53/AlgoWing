import sys
sys.stdin=open("sample_input.txt",'r')
def dfs(x,y):
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    # if x==1 and y==1:
    #     print()
    for i in range(4):
        next_x=x+dx[i]
        next_y=y+dy[i]
        if 0<=next_y<N and 0<=next_x<N:

            if road[next_x][next_y]-road[x][y]>=0:
                slope=road[next_x][next_y]-road[x][y]
            else:
                slope=0

            if 1+slope+ans[x][y] < ans[next_x][next_y] :
                # for temp in range(next_y+1,N):
                #     if 1+slope+ans[x][y]>ans[next_x][temp]:
                #         return
                ans[next_x][next_y]=1+slope+ans[x][y]
                dfs(next_x,next_y)

    return

T=int(input())

for test_case in range(1,T+1):
    N=int(input())
    road=[]
    for _ in range(N):
        road.append(list(map(int,input().split())))
    ans=[[float("inf")]*N for _ in range(N)]
    ans[0][0]=0
    x,y=0,0
    dfs(x,y)
    # print(ans)
    print("#{} {}".format(test_case,ans[N-1][N-1]))



#오른쪽과 아래로만 가게하면 런타임 에러는 나지 않으나 오답이 뜸(아마 왼쪽/위쪽으로 가는 루트가 정답일 경우 같음)
#4방향으로 다 가게되면 언제 가지를 쳐야할지 잘 모르겠음.