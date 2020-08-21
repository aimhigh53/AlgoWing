# 24시간 운영되는 물류센터에는 화물을 싣고 내리는 도크가 설치되어 있다.
#
# 0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면, 최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램을 만드시오.
#
# 신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있고, 앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.
#
# 예를 들어 앞 작업의 종료 시간이 5시면 다음 작업의 시작 시간은 5시부터 가능하다.


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