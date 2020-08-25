
import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    truck.sort(reverse=True)
    container.sort(reverse=True)
    # print(container)
    # print(truck)

    moved = []
    for i in container:
        for j in truck:
            if j >= i:
                moved.append(i)
                truck.remove(j)
                break
    # print(moved)

    print('#{} {}'.format(test_case, sum(moved)))
