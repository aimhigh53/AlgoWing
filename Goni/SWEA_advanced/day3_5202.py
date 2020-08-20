import sys
sys.stdin=open("sample_input.txt","r")

T=int(input())

for test_case in range(1,T+1):
    N=int(input())
    times=[]
    for _ in range(N):
        times.append(list(map(int,input().split())))

    times.sort(key=lambda x: x[0])
    times.sort(key=lambda x: x[1])
    ans = [times[0]]

    i=0
    k=1
    while(i<N and k<N):
        if times[i][1]<=times[k][0]:
            ans.append(times[k])
            i=k
        k+=1
    print("#", test_case, sep='', end=' ')
    print(len(ans))