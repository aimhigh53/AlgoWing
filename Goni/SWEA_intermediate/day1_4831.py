import sys
sys.stdin=open("sample_input.txt",'r')

T = int(input())

for test_case in range(1, 1 + T):
    K, N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    station = [0] * N
    for i in temp:
        station[i] = 1
    now = K
    count = 1
    while (True):
        now += K
        if now >= N:
            print("#", test_case, sep='', end=' ')
            print(count)
            break

        if station[now] == 1:
            count += 1
        else:
            for j in range(1, K):
                temp = count
                now -= 1
                if station[now] == 1:
                    count += 1
                    break

            if temp == count:
                print("#", test_case, sep='', end=' ')
                print('0')
                break