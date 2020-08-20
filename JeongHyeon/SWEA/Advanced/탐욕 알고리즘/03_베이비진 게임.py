## 03_베이비진 게임
'''
0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때, 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.
게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져가며, 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.
두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램을 작성하시오. 만약 무승부인 경우 0을 출력한다.
예를 들어 9 9 5 6 5 6 1 1 4 2 2 1인 경우, 플레이어 1은 9, 5, 5, 1, 4, 2카드를, 플레이어2는 9, 6, 6, 1, 2, 1을 가져가게 된다.
이때는 카드를 모두 가져갈 때 까지 run이나 triplet이 없으므로 무승부가 된다.
'''

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