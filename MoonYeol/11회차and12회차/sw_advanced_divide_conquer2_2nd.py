def quickSort(arr, n, left, right):
    if left >= right: return arr[left]
    pivot = left
    toChange = left

    for i in range(left + 1, right+1):
        if arr[pivot] >= arr[i]:
            toChange += 1
            arr[toChange], arr[i] = arr[i], arr[toChange]
    arr[toChange], arr[pivot] = arr[pivot], arr[toChange]
    pivot = toChange
    if pivot == n:
        return arr[pivot]
    elif pivot > n:
        return quickSort(arr, n, left, pivot - 1)
    else:
        return quickSort(arr, n, pivot + 1, right)


num = int(input())
numbers = []

for i in range(num):
    n = int(input())
    numbers.append(list(map(int, input().split())))


for idx, i in enumerate(numbers):
    answer = quickSort(i, len(i)//2,0, len(i) -1)
    print("#" + str(idx+1) +" " + str(answer) )
