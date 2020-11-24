import sys

inp = sys.stdin.readline

t = int(inp())

for tc in range(t):
    n = int(inp())
    a = [0]+[*map(int, inp().split())]
    ch = [-1]*(n+1)
    for student_num in range(1, n + 1):
        reached = []
        cur_position = student_num
        while (ch[cur_position] == -1):
            ch[cur_position] = 1
            reached.append(cur_position)
            cur_position = a[cur_position]
        while (ch[cur_position] == 1):
            ch[cur_position] = 2
            cur_position = a[cur_position]
        for k in reached:
            if (ch[k] != 2): ch[k] = 0
    print(n-ch.count(2))
