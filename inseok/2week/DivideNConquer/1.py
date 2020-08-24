
    
def sol(dqlist):
    global cnt
    if len(dqlist)<=1:
        cnt=0
        return dqlist
    else:
        lidx=0
        ridx=0
        
        rightlist=sol(dqlist[len(dqlist)//2:])
        leftlist=sol(dqlist[:len(dqlist)//2])
        
        tmplist=[]
        #합치는 부분
        for _ in range(len(dqlist)):
            #순서 바꾸면 인덱스 애러
            if lidx==len(leftlist):
                tmplist.append(rightlist[ridx])
                ridx+=1
            elif ridx==len(rightlist):
                tmplist.append(leftlist[lidx])
                lidx+=1
            
            elif leftlist[lidx]>=rightlist[ridx]:
                tmplist.append(rightlist[ridx])    
                ridx+=1

            elif leftlist[lidx]<=rightlist[ridx]:
                tmplist.append(leftlist[lidx])  
                lidx+=1
            

            
        return tmplist


T = int(input())
##cnt문제

for test_case in range(1, T + 1):
    N = int(input())
    dqlist = list(map(int, input().split()))
    cnt=0
    sortedList=sol(dqlist)
    print(sortedList[N//2])
