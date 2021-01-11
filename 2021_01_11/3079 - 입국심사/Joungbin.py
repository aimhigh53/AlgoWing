import sys

inp = sys.stdin.readline

n, m = map(int, inp().split())
dur = []
for i in range(n):
    dur.append(int(inp()))

dur.sort()

l, r = 1, 2 ** 64 - 1
while (l < r):
    mid = (l + r) // 2
    s = 0
    for i in range(n):
        s += (mid // dur[i])
    if (s >= m):
        r = mid
    else:
        l = mid + 1

print(r)
