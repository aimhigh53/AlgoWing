Testcase=int(input())

#recursive
def sol(i):
    if i==1:
        return
    if nodelist[i//2]!=0:
        return
    #자식이 1개니 2개니
    #홀수일 때
    if (i-1)//2==i//2:
        nodelist[i//2]=nodelist[i]+nodelist[i-1]
    
    else:
        nodelist[i//2]=nodelist[i]
    
    
#     if i%2!=0:
#         nodelist[i//2]=nodelist[i]+nodelist[i-1]
    
#     #짝수일 때
#     else:
#         if nodelist[i+1]!=0:
#             nodelist[i//2]=nodelist[i+1]+nodelist[i]
#         else:
#             nodelist[i//2]=nodelist[i]
    
    
    
    


for tc in range(1,1+Testcase):
    nodecount,leafcount,outputnode=map(int,input().split(' '))
    
    nodelist=[0]*(nodecount+1)
    
    for _ in range(leafcount):
        leafnode,val=map(int,input().split(' '))
        nodelist[leafnode]=val
        
    
    for i in range(nodecount,1,-1):
        sol(i)

    print("#{} {}".format(tc,nodelist[outputnode]))
    
