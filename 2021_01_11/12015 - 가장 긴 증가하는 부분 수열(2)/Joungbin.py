# --------------Normal--------------
n = int(input())
input_list = [*map(int, input().split())]
lis = [input_list[0]]

for i in range(1, n):
    k = input_list[i]
    if (k > lis[-1]):
        lis.append(k)
    else:
        l, r = 0, len(lis) - 1
        mid = 0
        while (l < r):
            mid = (l + r) // 2
            x = lis[mid]
            if (k == x): break
            if (k > x):
                l = mid + 1
            else:
                r = mid
        if (k < lis[l]): lis[l] = k

print(len(lis))


# ---------Using 'Bisect'----------
from bisect import bisect

n = int(input())
input_list = [*map(int, input().split())]
inf = 2 * 10 ** 9
lis = [inf] * (len(input_list) + 1)

for i in range(n):
    x = bisect(lis, input_list[i])
    if (x > 0 and lis[x - 1] == input_list[i]): continue
    if (lis[x] == inf or lis[x] > input_list[i]): lis[x] = input_list[i]

print(lis.index(inf))
