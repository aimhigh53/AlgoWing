n = int(input())
a = [*map(int, input().split())]
a.sort()
able = a[0]

if (able != 1): # 최솟값이 1이 아닌 경우 1을 잴 수 없으므로
    able = 0 # 0으로 설정
else:
    for i in range(1, n): # 합을 더해가며 계산
        if (a[i] <= able + 1):
            able += a[i]
        else:
            break
print(able + 1)
