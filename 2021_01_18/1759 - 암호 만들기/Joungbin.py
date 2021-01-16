from itertools import combinations as com

n, m = map(int, input().split())
a = [*map(str, input().split())]
vow = ['a', 'e', 'i', 'o', 'u']
a.sort()

l = list(com(a, n))
for i in l:
    s = ''
    c, v = 0, 0
    for j in i:
        if (j in vow):
            v += 1
        else:
            c += 1
        s += j
    if (c > 1 and v > 0): print(s)

# c는 자음의 개수, v는 모음의 개수