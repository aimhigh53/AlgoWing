t=int(input())

for tc in range(t) :
    cards = list(map(int, input().split()))
    a = [0]*10
    b = [0]*10 # a와 b의 연속된 카드의 개수 체크
    ans = 0
    for card in range(6):
        a[cards[2 * card]] += 1
        if(3 in a):
            ans = 1 # a의 승리
            break
        for a_cards in range(8):
            if(a[a_cards] > 0 and a[a_cards + 1] > 0 and a[a_cards + 2] > 0):
                ans = 1
                break
        if(ans != 0):
            break
        b[cards[2 * card + 1]] += 1
        if(3 in b):
            ans = 2 # b의 승리
            break
        for b_cards in range(8):
            if(b[b_cards] > 0 and b[b_cards + 1] > 0 and b[b_cards + 2] > 0):
                ans = 2
                break
        if(ans!=0):
            break
    print('#%d' % (tc+1), ans)
