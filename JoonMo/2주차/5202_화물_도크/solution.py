
import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    schedule = []
    for _ in range(N):
        s, e = map(int, input().split())
        schedule.append((s,e))
        sorted_schedule = sorted(schedule, key = lambda x: (x[1], x[0]))
    # print(sorted_schedule)

    final_schedule = []
    start = 0
    for i in sorted_schedule:
        if i[0] >= start:
            final_schedule.append(i)
            start = i[1]
    # print(final_schedule)

    print('#{} {}'.format(test_case, len(final_schedule)))