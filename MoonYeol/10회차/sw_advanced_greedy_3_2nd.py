def findPlayer(player1,player2,player):
    if player == player1:
        return 1
    else:
        return 2


def solution(card):
    player1 = [0 for x in range(10)]
    player2 = [0 for x in range(10)]
    player = None
    for i in range(len(card)):
        if i % 2 == 0:
            player = player1
        else:
            player = player2

        player[card[i]] += 1

        if player[card[i]] >= 3:
                break
        else:
            if card[i] < 8:
                if player[card[i] + 1] and player[card[i] + 2]:
                    break
            if card[i] > 2:
                if player[card[i] - 1] and player[card[i] - 2]:
                    break
            if card[i] != 0 and card[i] != 9:
                if player[card[i] + 1] and player[card[i] - 1]:
                    break
    else:
        return 0
    return findPlayer(player1, player2, player)



num = int(input())
cards = []

for i in range(num):
    cards.append(list(map(int, input().split())))

for idx, i in enumerate(cards):
    answer = solution(i)
    print("#" + str(idx + 1) + " " + str(answer))
