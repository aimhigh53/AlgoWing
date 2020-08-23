## 02_화물 도크

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