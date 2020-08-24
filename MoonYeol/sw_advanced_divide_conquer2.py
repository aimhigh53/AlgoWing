def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, equals, right = [], [], []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equals.append(num)
    return quick(left) + equals + quick(right)


def quick2(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left, equals, right = [], [], []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equals.append(num)
    return quick2(left) + equals + quick2(right)

def quick3(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]

    return quick3(left) + [pivot] + quick3(right)

def quick4(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left, right = [], []
    for num in arr[1:]:
        if num <= pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)

    return quick2(left) + [pivot] + quick2(right)

num = int(input())
numbers = []

for i in range(num):
    n = int(input())
    numbers.append(list(map(int, input().split())))


for idx, i in enumerate(numbers):
    answer = quick4(i)
    print("#" + str(idx+1) +" " + str(answer[len(answer)//2]) )
