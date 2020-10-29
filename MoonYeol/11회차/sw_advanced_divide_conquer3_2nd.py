def binary_search(num, A, left, right, flag):
    if left > right:
        return 0
    else:
        mid = (left + right) // 2
        if A[mid] == num:
            return 1
        elif A[mid] > num:
            if flag == -1:
                return 0
            return binary_search(num, A, left, mid - 1, -1)
        elif A[mid] < num:
            if flag == 1:
                return 0
            return binary_search(num, A, mid + 1, right, 1)


T = int(input())
As = []
Bs = []

for i in range(T):
    n, m = map(int, input().split())
    As.append(sorted(map(int, input().split())))
    Bs.append(list(map(int, input().split())))

for idx, A in enumerate(As):
    answer = 0
    for num in Bs[idx]:
        answer += binary_search(num, A, 0, len(i) - 1, 0)
    print("#" + str(idx + 1) + " " + str(answer))
