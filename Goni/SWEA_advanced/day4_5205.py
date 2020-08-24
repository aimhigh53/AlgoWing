import sys
sys.stdin=open("sample_input.txt","r")

T=int(input())
def quicksort(lst):
    left=[]
    right=[]
    mid=[]
    if len(lst)<=1:
        return lst
    pivot=lst[len(lst)//2]
    for i in lst:
        if i<pivot:
            left.append(i)
        elif i>pivot:
            right.append(i)
        else:
            mid.append(i)
    return quicksort(left)+mid+quicksort(right)



for test_case in range(1,T+1):
    N=int(input())
    unsorted_list=list(map(int,input().split()))

    print("#",test_case,sep='',end=' ')
    print(quicksort(unsorted_list)[N//2])

#  1개 케이스 계속 오류남
