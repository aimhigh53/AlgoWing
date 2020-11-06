
def merge(left, right):
    result= []
    global count
    leftIdx, rightIdx = 0, 0
    if left[-1] > right[-1]:
         count +=1
    while len(left) > leftIdx or len(right) > rightIdx:
        if len(left) > leftIdx and len(right) > rightIdx:
            if left[leftIdx] <= right[rightIdx]:
                result.append(left[leftIdx])
                leftIdx += 1
            else:
                result.append(right[rightIdx])
                rightIdx += 1
        elif len(left) > leftIdx:
            result.append(left[leftIdx])
            leftIdx += 1
        elif len(right) > rightIdx:
            result.append(right[rightIdx])
            rightIdx +=1
    return result

def merge_sort(numbers):
    if len(numbers)<=1:
        return numbers
    mid = len(numbers)//2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])
    result = merge(left,right)
    return result


num = int(input())
numbers = []
count = 0
for i in range(num):
    n = int(input())
    numbers.append(list(map(int, input().split())))


for idx, i in enumerate(numbers):
    answer = merge_sort(i)
    print("#" + str(idx+1) +" " + str(answer[len(answer)//2]) + " " + str(count))
    count = 0