Testcase=int(input())

#root지정 후
#left,right확인
#이를 왼,오 각각 실행

#자식>부모 조건
def sol(i):
    #얘의 역할은 부모와 자식간 크기를 비교해서
    #위치를 변경
    #부모가 i일때 왼은 2i 오는 2i+1
    if i>N:
        #탈출조건
        return
    
    
    if i==1:
        ansList[1]=verList[i]

    elif i>1:
        #부모가 크다면
        if ansList[i//2]>verList[i]:
            ansList[i//2],ansList[i]=verList[i],ansList[i//2]
        else:
            ansList[i]=verList[i]
            
    
    sol(2*i)
    sol(2*i+1)
    


for tc in range(1,1+Testcase):
    N=int(input())
    verList=list(map(int,input().split(' ')))
    verList.insert(0,0)
    answer=0
    
    ansList=[0]*(N+1)
    sol(1)
#     ansList.remove(0)
    
    
    while N>0:
        N=N//2
        answer+=ansList[N]

    print("#{} {}".format(tc,answer))
    
#     for i in range((N//2)-1):
#         answer+=ansList[2*i]
#     print(ansList)
#     print(answer)
    
