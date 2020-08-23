## 01_컨테이너 운반

T = int(input())

for test_case in range(1, T + 1):
    # con_n : 컨테이너 수/ truck_n : 트럭 수
    con_n, truck_n = map(int, input().split())

    # 컨테이너 무게
    con_w = list(map(int, input().split()))
    con_w.sort(reverse=True)

    # 트럭 적재용량
    truck_w = list(map(int, input().split()))
    truck_w.sort(reverse=True)

    # 옮겨진 화물의 전체 무게
    answer = 0

    # 트럭 기준 오름차순 비교
    for i in truck_w:
        for j in range(len(con_w)):
            if i >= con_w[j]:
                answer += con_w[j]
                con_w.remove(con_w[j])
                break
            elif len(con_w) == 0:
                break
            else:
                continue
        if len(con_w) == 0:
            break
    print('#{} {}'.format(test_case, answer))