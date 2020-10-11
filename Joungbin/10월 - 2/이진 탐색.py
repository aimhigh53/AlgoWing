t = int(input())

for tc in range(t) :
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(len(b)):
        start, end = 0, n - 1
        interval = 0
        while(start <= end):
            mid= (start + end)//2
            if(b[i] == a[mid]): # 가운데 값일 때는 방향을 따지지 않음
                ans += 1
                break
            else:
                if(b[i] < a[mid]): # 다음에 선택해야 하는 구간이 왼쪽인 경우
                    if(interval == -1): # 같은 구간을 연속으로 두 번 선택할 수 없음
                        break
                    end = mid - 1
                    interval = -1
                else:
                    if(interval == 1):
                        break
                    start = mid + 1
                    interval = 1
    print('#%d' % (tc+1), ans)
