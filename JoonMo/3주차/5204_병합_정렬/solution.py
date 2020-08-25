import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')



# 출처: https://ratsgo.github.io/data%20structure&algorithm/2017/10/03/mergesort/
def merge(left, right):
    result = []
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

def merge_sort(lst):
    global cnt
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    leftList = lst[:mid]
    rightList = lst[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)



T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    lst = merge_sort(lst)
    # print(lst)

    print('#{} {} {}'.format(test_case, lst[N//2], cnt))