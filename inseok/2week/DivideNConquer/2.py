def sol(anslist,left,right):
    if left < right:
        pivot= divide(anslist,left,right)
        if pivot==N//2:
            return 
        elif pivot>N//2:
            sol(anslist,left, pivot - 1)
        elif pivot<N//2:
            sol(anslist,pivot+1,right)

def divide(anslist,left,right):
    pivot = (left+right)// 2
    while left<right :
        while(left<right and anslist[left]<anslist[pivot]):
            left+=1
        while(left<right and anslist[right]>=anslist[pivot]) :
            right-=1
        if left < right:
            if left == pivot:
                pivot = right
            tmp=anslist[left]
            anslist[left]=anslist[right]
            anslist[right]=tmp
    
    tmp=anslist[pivot]
    anslist[pivot]=anslist[right] 
    anslist[right]=tmp
    
    return right



T = int(input())
for tc in range(0,T):
    N = int(input())
    anslist = list(map(int, input().split()))
    sol(anslist, 0, N - 1)
    print('#{} {}'.format(tc+1, anslist[N//2]))
