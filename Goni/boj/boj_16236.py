# def isBound(y,x):
#     if 0<=y<N and 0<=x<N and visited[y][x]!=1:
#         return True
#     else:
#         return False
#
# def findFoodCandi(y,x):
#     for k in range(4):
#         nowY=y+dy[k]
#         nowX=x+dx[k]
#         if isBound(nowY,nowX):
#
#             if 0<box[nowY][nowX]<size:
#                 candi.append([nowY, nowX])
#                 visited[nowY][nowX]=1
#                 findFoodCandi(nowY,nowX)
#             elif box[nowY][nowX]==0 or box[nowY][nowX]==size:
#                 visited[nowY][nowX]=1
#                 findFoodCandi(nowY,nowX)
#
#
# N=int(input())
# box=[]
# shark=[0,0]
# size=2
# dx=[0,-1,0,1]
# dy=[-1,0,1,0]
#
# for y in range(N):
#     temp=list(map(int,input().split()))
#     box.append(temp)
#     for index,num in enumerate(temp):
#         if num==9:
#             shark[0] = y
#             shark[1] = index
#             break
# checkSize=0
# ans=0
# ate=0
# while(True):
#     visited = [[0] * N for _ in range(N)]
#     candi = []
#     distance=400
#     findFoodCandi(shark[0],shark[1])
#     if (candi):
#         for each in candi:
#             now=abs(shark[0]-each[0])+abs(shark[1]-each[1])
#             if now<distance:
#                 distance=now
#                 food=each
#         box[food[0]][food[1]]=0
#         ans+=distance
#         ate+=1
#         shark=food[:]
#
#         if ate==size:
#             size+=1
#             ate=0
#     else:
#         break
#
#
# print(ans)
def isBound(y,x):
    if 0<=y<N and 0<=x<N and visited[y][x]!=1:
        return True
    else:
        return False

def findFood(y,x):
    breaker = False
    while(stack):
        y=stack[0][0]
        x=stack[0][1]
        tempans=stack[0][2]
        tempans += 1
        stack.pop(0)
        if visited[y][x]==0:
            visited[y][x]=1
            for i in range(4):
                nowY=y+dy[i]
                nowX=x+dx[i]
                if isBound(nowY,nowX):
                    if 0 < box[nowY][nowX] < size:
                        stack.append([nowY, nowX,tempans])
                        breaker=True
                        break
                    elif box[nowY][nowX]==0 :
                        stack.append([nowY, nowX,tempans])
                    elif box[nowY][nowX]==size:
                        breaker=True
                        break


        if breaker==True:
            break

    if breaker==True:
        return True
    else:
        return False


N=int(input())
box=[]
shark=[-1,-1]
size=2
ate=0
dx=[0,-1,0,1]
dy=[-1,0,1,0]
visited = [[0] * N for _ in range(N)]

for y in range(N):
    temp=list(map(int,input().split()))
    box.append(temp)
    if shark[0]==-1:
        for index,num in enumerate(temp):
            if num==9:
                shark[0] = y
                shark[1] = index
                box[shark[0]][shark[1]]=0
                break

stack=[[shark[0],shark[1],0]]
ans=0
while(True):
    if findFood(shark[0],shark[1]):
        shark=[stack[-1][0],stack[-1][1]]
        ans=stack[-1][2]
        stack=[[stack[-1][0],stack[-1][1],stack[-1][2]]]
        box[stack[-1][0]][stack[-1][1]]=0
        visited = [[0] * N for _ in range(N)]
        print(shark,stack)
        ate+=1
        if ate==size:
            ate=0
            size+=1
    else:
        print(ans)
        break

