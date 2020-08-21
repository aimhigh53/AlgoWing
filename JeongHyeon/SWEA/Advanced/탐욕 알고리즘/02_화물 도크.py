## 02_화물 도크
'''
24시간 운영되는 물류센터에는 화물을 싣고 내리는 도크가 설치되어 있다.
0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면, 최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램을 만드시오.
신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있고, 앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.
예를 들어 앞 작업의 종료 시간이 5시면 다음 작업의 시작 시간은 5시부터 가능하다.
'''

T = int(input())

for test_case in range(1, T + 1):
    # 신청서 수
    n = int(input())

    # n개의 [시작시간, 종료시간]
    # 종료시간 기준 오름차순 정렬
    truck = []
    for _ in range(n):
        truck.append(list(map(int, input().split())))
    truck_sorted = sorted(truck, key=lambda x: x[1])
    # print(truck)
    # print(truck_sorted)

    # 최대 이용 화물차 수
    answer = 0

    # 가장 빨리 종료되는 작업 찾기
    while True:
        end_time = truck_sorted[0][1]
        truck_sorted.remove(truck_sorted[0])
        answer += 1

        # 시작시간:i[0] < 종료시간 제거
        for i in truck_sorted[:]: # [:] : remove하여 index 건너뛰는 문제 예방
            if i[0] < end_time:
                truck_sorted.remove(i)
        # for i in range(len(truck_sorted)):
        #     if truck_sorted[i][0] < end_time:
        #         truck_sorted.remove(truck_sorted[i])
        #         i -= 1

        if len(truck_sorted) == 0:
            break

    print('#{} {}'.format(test_case, answer))