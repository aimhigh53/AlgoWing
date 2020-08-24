def binary_search(num,arr,left,right,flag):
    if left > right:
        return 0
    else :
        mid = (left + right) // 2
        if arr[mid] == num:

            return 1
        elif arr[mid] > num:
            if flag == -1:
                return 0
            return binary_search(num,arr,left,mid-1,-1)
        elif arr[mid] < num:
            if flag == 1:
                return 0
            return binary_search(num,arr,mid+1,right,1)



num = int(input())
A = []
B = []


for i in range(num):
    n,m = map(int,input().split())
    A.append(sorted(map(int, input().split())))
    B.append(list(map(int, input().split())))

for idx, i in enumerate(A):
    answer = 0
    for j in B[idx] :
        answer += binary_search(j,i,0,len(i)-1,0)
    print("#" + str(idx+1) +" " + str(answer) )
