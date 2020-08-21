## 01_컨테이너 운반
'''
화물이 실려 있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 한다.
트럭당 한 개의 컨테이너를 운반 할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.
컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어지고, A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행한다고 한다.
이때 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램을 만드시오.
화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다. 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.
'''

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