## 4831. 전기버스
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

T = int(input())
for test_case in range(1, T + 1):

    # 최대 이동 수, 정류장 수, 충전소 수
    max_move, station, charge_num = map(int, input().split())
    # 충전소 위치
    charge_list = list(map(int, input().split()))

    answer = 0
    before_charge = 0
    for i in range(len(charge_list)):
        # 충전소 잘못 설치
        if charge_list[i]-before_charge > max_move:
            answer = 0
            break
        # 마지막 충전소
        elif i == len(charge_list)-1:
            if charge_list[i] + max_move < station: # 도착지 도달 못함
                answer = 0
                break
            elif station - before_charge > max_move: # 충전 & 도착
                answer += 1
            else: # 충전x & 도착
                continue
        # 충전 안해도 됨
        elif charge_list[i+1] - before_charge <= max_move:
            continue
        # 충전
        else:
            answer += 1
            before_charge = charge_list[i]

    print('#' + str(test_case), answer)