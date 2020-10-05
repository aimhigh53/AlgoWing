import sys
sys.stdin=open("sample_input.txt",'r')

def tripletCheck(lst):
    lst.sort()

    for index in range(len(lst)-2):
        if lst[index]==lst[index+1]:
            if lst[index]==lst[index+2]:
                return True

def runCheck(lst):
    lst=list(set(lst))
    lst.sort()
    for index in range(len(lst)-2):
        if lst[index]+1==lst[index+1]:
            if lst[index]+2==lst[index+2]:
                return True

T=int(input())
for test_case in range(1,T+1):
    cards=list(map(int,input().split()))
    playerA,playerB=[],[]
    for i in range(0,len(cards)-1,2):
        playerA.append(cards[i])
        playerB.append(cards[i+1])

    for i in range(3,7):
        if tripletCheck(playerA[0:i]):
            print("#{} {}".format(test_case,'1' ))
            break
        elif runCheck(playerA[0:i]):
            print("#{} {}".format(test_case, '1'))
            break
        if tripletCheck(playerB[0:i]):
            print("#{} {}".format(test_case, '2'))
            break
        elif runCheck(playerB[0:i]):
            print("#{} {}".format(test_case,'2'))
            break

        if i==6:
            print("#{} {}".format(test_case, '0'))

