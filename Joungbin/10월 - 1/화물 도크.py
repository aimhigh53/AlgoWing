t = int(input())

for tc in range(t):
    n = int(input())
    time = [[*map(int, input().split())] for _ in range(n)]
    ans = 0
    time.sort(key=lambda x: (x[1], x[0]))
    start = time[0][0]
    for i in range(n):
        if(start <= time[i][0]):
            start = time[i][1]
            ans += 1
    print('#%d' % (tc+1), ans)
