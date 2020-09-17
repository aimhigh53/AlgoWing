Testcase=int(input())
 
# def findparent(x):
#     if 
 
def sol(arr,idx):
    global cnt
#     if idx in arr:
    tmplist=list(filter(lambda x: arr[x] == idx, range(len(arr))))
    if tmplist:
        for i in tmplist:
            cnt+=1
            sol(arr,i)
    return
 
 
 
for tc in range(1,1+Testcase):
    E,N=map(int,input().split(' '))
    inputlist=list(map(int,input().split(' ')))
    parentchildlist=[0]*(E+2)
    cnt=1
    
    s=0
    for i in inputlist[1::2]:
        parentchildlist[i]=inputlist[2*s]
        s+=1
        


#     for i in range(E):
#         parentchildlist[inputlist[2*i+1]]=inputlist[2*i]
    sol(parentchildlist,N)
 
 
 
    print("#{} {}".format(tc,cnt))
