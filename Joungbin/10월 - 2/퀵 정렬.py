t = int(input())

def quicksort(start, end):
    if(start >= end): return
    mid = (start + end)//2
    pivot = a[mid] # 피벗을 하나 정한 다음
    idx = start # 인덱스를 맨 왼쪽 위치로 잡음
    a[mid], a[end] = a[end], a[mid] # Swap, 피벗의 값을 맨 오른쪽에 두기 위한 과정

    for i in range(start, end): # 피벗이 맨 오른쪽에 있으므로 그 바로 전까지만 진행
        if(a[i] < pivot): # 크기가 피벗보다 더 작은 경우 왼쪽으로 보냄
            a[i], a[idx] = a[idx], a[i] # Swap
            idx += 1
    a[idx], a[end] = a[end], a[idx] # 최종적으로 idx번째가 피벗이 들어갈 자리
    quicksort(start, idx-1)
    quicksort(idx+1, end)


for tc in range(t):
    n = int(input())
    a = [*map(int, input().split())]
    quicksort(0, n-1)
    print('#%d' % (tc+1), a[n//2])
