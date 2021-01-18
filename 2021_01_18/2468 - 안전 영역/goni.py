'''
sys.setrecursionlimit()를 무조건 추가해줘야한다는 글이 있던데 안써도 잘만 되더라...
모든 높이에 대해서 매번 모든 영역을 돌아보며 확인해줬다.
dfs 함수 한번 돌 때마다 영역 하나 추가
'''
n=int(input())
box=[]
for _ in range(n):
    box.append(list(map(int,input().split())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(i,j):
    stack=[[i,j]]
    while(stack):
        temp=stack.pop()
        nowi=temp[0]
        nowj=temp[1]
        visited[nowi][nowj]=1

        for c in range(4):
            nexti=nowi+dx[c]
            nextj=nowj+dy[c]
            if isBound(nexti,nextj):
                if box[nexti][nextj]>h and visited[nexti][nextj]==0:
                    stack.append([nexti,nextj])

def isBound(i,j):
    if 0<=i<n and 0<=j<n:
        return True
    else:
        return False

max=1
for h in range(1,101):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    count=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0 and box[i][j]>h:
                dfs(i,j)
                count+=1
    if count>max:
        max=count

print(max)
