import sys
sys.stdin=open("sample_input.txt",'r')

T=int(input())

for test_case in range(1,T+1):
    ans=0
    container_num,truck_num=map(int,input().split())
    baggage_weight=list(map(int,input().split()))
    truck_weight=list(map(int,input().split()))

    baggage_weight.sort(reverse=True)
    truck_weight.sort(reverse=True)

    i,j=0,0
    while(i<truck_num and j<container_num):
        if truck_weight[i]>=baggage_weight[j]:
            ans+=baggage_weight[j]
            i+=1
            j+=1
        else:
            j+=1

    print("#{} {}".format(test_case,ans))

