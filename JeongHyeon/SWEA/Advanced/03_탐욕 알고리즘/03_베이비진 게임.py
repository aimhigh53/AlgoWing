## 03_베이비진 게임

# run 판별
def run_check(list):
    temp = 0
    for i in list:
        if i != 0:
            temp += 1
            if temp >= 3:
                return True
        else: # 초기화
            temp = 0
    return False

T = int(input())

for test_case in range(1, T + 1):

    one = [0] * 10  # 플레이어1
    two = [0] * 10  # 플레이어2
    card = list(map(int, input().split()))

    answer = ''
    # 카드 분배
    for i in range(12):
        if i % 2 == 0:
            one[card[i]] += 1
        else:
            two[card[i]] += 1
        # print(one)
        # print(two)

        # 승자 확인
        if i >= 5: # 1인당 최소 3장 가지고 있을 때

            # triplet & run
            if one.count(3) >= 1 or run_check(one):
                answer = 1
                break
            elif two.count(3) >= 1 or run_check(two):
                answer = 2
                break

            # 무승부
            elif i == 11:
                answer = 0
                break

    print('#{} {}'.format(test_case, answer))