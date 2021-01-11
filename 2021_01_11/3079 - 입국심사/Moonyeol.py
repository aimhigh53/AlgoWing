import sys

input = sys.stdin.readline


def binarySearch(l, r):
    result = 0
    while l <= r:
        m = (l + r) // 2
        done = 0
        for T in Ts:
            done += m // T
        if done >= M:
            r = m - 1
            result = m
        else:
            l = m + 1
    return result


N, M = map(int, input().split())
Ts = []
for _ in range(N):
    Ts.append(int(input()))

min_T = max(Ts)

print(binarySearch(0, min_T * M))
