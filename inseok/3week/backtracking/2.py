Testcase=int(input())
#선택을,,, 모든 경우를 다 돌것인가
#아님 선택해서 돌것인가

#들어갈 수 있는 곳의 최소를 찾아라

                
def findmin(i):

    tmp=0
    minval=1000
    for k in range(N):
        if check[k]==0:
            if minval>=field[i][k]:
                minval=field[i][k]
                tmp=k
                print(tmp)
    return minval,tmp
 
def sol(i,tot):
    global result
    
#     if i==N:
#         if result>tot:
#             result=tot
#         return
#     if result<tot:
#         return
    
    for i in range(N):
        minval,forcheck=findmin(i)
        check[forcheck]=1
        tot+=minval

for tc in range(1,Testcase+1):
    N=int(input())
    field=[list(map(int,input().split(' '))) for _ in range(N)]
#     check=[[0]*N for _ in range(N)]
    check=[0]*N
    result=9999999
    sol(0,0)
