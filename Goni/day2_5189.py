import sys
import itertools

sys.stdin=open("sample_input.txt","r")

T=int(input())

for test_case in range(1,T+1):
    N=int(input())
    battery=[]
    temp=[]
    for i in range(N):
        battery.append(list(map(int,input().split())))
        temp.append(i)
    temp.pop(0)
    #temp는 경로 구하려고 만듦, 첫번쨰 인덱스를 pop한건 사무실 오가는 따로 계산하려고.
    permu=list(itertools.permutations(temp))
    ans=[0]*len(permu)
    i=0
    for each in permu:
        for k in range(N-2):
            ans[i]+=battery[each[k]][each[k+1]]

        #사무실까지 가는건 따로 계산
        ans[i]+=battery[0][each[0]]
        ans[i]+=battery[each[-1]][0]
        i+=1

    print("#", test_case, sep='', end=' ')
    print(min(ans))








