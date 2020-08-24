import sys
sys.stdin=open("sample_input.txt","r")

T=int(input())
def dividing(lst):
    Len=len(lst)
    if Len<=1:
        return lst


    left=lst[0:Len//2]
    right=lst[Len//2:]

    left1=dividing(left)
    right1=dividing(right)

    return merging(left1,right1)

def merging(left,right):
    global count
    i,j=0,0
    sorted=[]

    while(True):
        if i==len(left):
            for k in range(j,len(right)):
                sorted.append(right[k])
            break
        elif j==len(right):
            for k in range(i,len(left)):
                sorted.append(left[k])
            count += 1
            break

        if left[i]>right[j]:
            sorted.append(right[j])
            j+=1
        else:
            sorted.append(left[i])
            i+=1

    return sorted



for test_case in range(1,T+1):

    count=0
    N=int(input())
    unsorted_list=list(map(int,input().split()))

    print("#",test_case,sep='',end=' ')
    print(dividing(unsorted_list)[N//2],end=' ')
    print(count)

