Testcase=int(input())
#itval: 충전지
#loc:현재위치
#cnt:움직인 횟수


def sol(itval,loc,cnt):
#     print(itval,loc,cnt)
#     print(trackList)
    for i in range(loc+1,loc+itval+1):
        if i<statList[0]:
            if trackList[i]==0:
#                 print(loc,'loc1')
                trackList[i]=cnt
                sol(statList[i],i,cnt+1)
            else:
                if trackList[i]>trackList[loc]+1:
#                     print(loc,i,'loc2')
                    trackList[i]=trackList[loc]+1
                    sol(statList[i],i,cnt)
#         elif i==statList[0]:
#             sol(statList[i],i,cnt)
            
            
           
for tc in range(1,Testcase+1):
    statList=[int(x) for x in input().split(' ')]
    trackList=[0]*(statList[0])
    sol(statList[1],1,0)
    
    print('#{} {}'.format(tc,trackList[statList[0]-1]))
