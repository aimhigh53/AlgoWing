import sys
sys.stdin=open("sample_input.txt",'r')

T=int(input())

for test_case in range(1,T+1):
    max,station_num,recharge_num=map(int,input().split())
    recharge_station=list(map(int,input().split()))
    now=0
    count=0
    breaker=False
    while(True):
        for i in range(max,0,-1):
            if now+max >= station_num:
                breaker=True
                break
            elif now+i in recharge_station:
                count+=1
                now+=i
                break
            if i==1:
                count=0
                breaker = True
                break
        if breaker:
            break




    print("#", test_case, sep='', end=' ')
    print(count)