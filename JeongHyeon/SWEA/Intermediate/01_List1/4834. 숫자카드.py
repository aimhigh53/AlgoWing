## 4834. 숫자카드
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num_array = [0]*103
    card_list = list(map(int, input()))

    for card in card_list :
        num_array[card] += 1

    how_many = max(num_array)
    many_card_num = num_array.index(how_many)

    # 카드 장수 같은 경우 check
    while num_array.count(how_many) != 1 :
        num_array[many_card_num] = 0
        temp = num_array.index(how_many)
        many_card_num = max(many_card_num, temp)

    print('#' + str(test_case), many_card_num, how_many)