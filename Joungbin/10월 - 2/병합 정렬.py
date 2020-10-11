t = int(input())

def mergesort(start, end):
    global count
    b = []
    mid = (start + end-1)//2
    i, j = start, mid+1 # i는 머지 왼쪽 부분의 시작점, j는 오른쪽 부분의 시작점
    if(a[mid]>a[end]) : count += 1 # 부분의 끝 값을 비교하여 왼쪽이 더 큰 경우 +1
    while(i<=mid and j<=end): # 병합 정렬 - 둘 모두 부분의 끝 점에 도착하지 않았을 때만 진행
        if(a[i]<=a[j]): # 왼쪽 값을 비교하여 더 작은 값이 먼저 들어감
            b.append(a[i])
            i += 1
        else: # 왼쪽이 큰 경우 i 증가, 오른쪽이 큰 경우 j 증가(투 포인터)
            b.append(a[j])
            j += 1
    while(i<=mid): # 둘 중 도달하지 않은 포인터가 있는 경우 계속해서 값을 넣어주면 됨
        b.append(a[i])
        i += 1
    while(j<=end):
        b.append(a[j])
        j += 1
    for x in range(start, end+1) : # a에는 원소가 다 들어있고, b에는 원소가 정렬되 채 일부만 들어있으므로
        a[x]=b[x - start] # start부터 end까지 진행

def division(start, end): # 계속해서 절반으로 나누는 과정
    if(start==end): return # 원소가 1개인 경우 진행하지 않음
    mid = (start + end-1)//2
    division(start, mid)
    division(mid+1, end)
    mergesort(start, end)

for tc in range(t):
    n = int(input())
    count = 0
    a = [*map(int, input().split())]
    division(0, n-1)
    print('#%d' % (tc+1), a[n//2], count)
