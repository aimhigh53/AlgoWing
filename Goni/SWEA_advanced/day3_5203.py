import sys
sys.stdin=open("sample_input.txt","r")
T=int(input())

for test_case in range(1,T+1):
    temp=list(map(int,input().split()))
    player1,player2=[],[]
    for i in range(0,11,2):
        player1.append(temp[i])
        player2.append(temp[i+1])

    for_check1,for_check2=[0]*10,[0]*10

    for i in range(3):
        for_check1[player1[i]]+=1
        for_check2[player2[i]]+=1

    flag=0
    for i in range(3,6,1):
        #player1 차례
        for_check1[player1[i]]+=1
        if 3 in for_check1: #런확인
            flag=1
            break
        else:#트리플확인
            for k in range(8):
                if for_check1[k]!=0 and for_check1[k+1]!=0 and for_check1[k+2]!=0:
                    flag=1
                    break
            if flag==1:
                break

        # player2 차례
        for_check2[player2[i]] += 1
        if 3 in for_check2: #런확인
            flag=2
            break
        else:#트리플확인
            for k in range(8):
                if for_check2[k]!=0 and for_check2[k+1]!=0 and for_check2[k+2]!=0:
                    flag=2
                    break
            if flag==2:
                break


    print("#",test_case,sep='',end=' ')
    print(flag)