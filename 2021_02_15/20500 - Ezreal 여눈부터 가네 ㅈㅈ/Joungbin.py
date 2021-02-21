n = int(input())
mod = 10 ** 9 + 7
d = [[1] * (n + 1) for _ in range(n + 1)]
# d[i][j]는 iCj(조합)
ans = 0

for i in range(2, n + 1):
    for j in range(1, i):
        d[i][j] = (d[i - 1][j - 1] + d[i - 1][j]) % mod

for i in range(n):
    if (abs(n - 2 * i) % 3 == 0): ans += d[n - 1][i]

print(ans % mod)
