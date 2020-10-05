import sys
sys.stdin=open("sample_input.txt",'r')

T=int(input())

for test_case in range(1,T+1):
    num=int(input())
    schedule=[]
    for _ in range(num):
        a,b=map(int,input().split())
        schedule.append([a,b])
    schedule=sorted(schedule,key=lambda x:x[1])
    ans=[schedule[0]]
    for each in schedule:
        if ans[-1][1]<=each[0]:
            ans.append(each)

    print("#{} {}".format(test_case,len(ans)))

