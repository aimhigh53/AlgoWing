

def solution(card):
    player1 = [0 for x in range(10)]
    player2 = [0 for x in range(10)]

    for i in range(len(card)):
        if i % 2 == 0:
            player1[card[i]] += 1
            if player1[card[i]] >=3:
                return 1
            else:
                if card[i] < 8:
                    if player1[card[i]+1] and player1[card[i]+2] :
                        return 1
                if card[i] > 2:
                    if player1[card[i] - 1] and player1[card[i] - 2]:
                        return 1
                if card[i] != 0 and card[i] != 9 :
                    if player1[card[i] +1]  and player1[card[i]-1]:
                        return 1
        else :
            player2[card[i]] += 1
            if player2[card[i]] >=3 :
                return 2
            else:
                if card[i] < 8:
                    if player2[card[i]+1] and player2[card[i]+2] :
                        return 2
                if card[i] > 2:
                    if player2[card[i] - 1] and player2[card[i] - 2]:
                        return 2
                if card[i] != 0 and card[i] != 9 :
                    if player2[card[i] +1 ] and player2[card[i]-1]:
                        return 2
    return 0


num = int(input())
cards = []

for i in range(num):
    cards.append(list(map(int, input().split())))

for idx, i in enumerate(cards):
    answer = solution(i)
    print("#" + str(idx+1) +" " + str(answer))
