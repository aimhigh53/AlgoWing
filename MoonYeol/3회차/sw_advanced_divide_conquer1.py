
def merge(left, right):
    result= []
    global count
    i, j = 0, 0
    if left[-1] > right[-1]:
         count +=1
    while len(left) > i or len(right) > j:
        if len(left) > i and len(right) > j:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif len(left) > i:
            result.append(left[i])
            i += 1
        elif len(right) > j:
            result.append(right[j])
            j +=1
    return result

def solution(numbers):
    if len(numbers)<=1:
        return numbers
    left = solution(numbers[:len(numbers)//2])
    right = solution(numbers[len(numbers) // 2:])
    result = merge(left,right)
    return result


num = int(input())
numbers = []
count = 0
for i in range(num):
    n = int(input())
    numbers.append(list(map(int, input().split())))


for idx, i in enumerate(numbers):
    answer = solution(i)
    print("#" + str(idx+1) +" " + str(answer[len(answer)//2]) + " " + str(count))
    count = 0