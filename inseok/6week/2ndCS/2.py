Testcase=int(input())
 
#dfs로 해결
#1-순열-1
#근데 다 돌아야함
#N=3 1-2-3-1
 
#현재 것을 담고 전진, 뒤로

#탐험했는지 표시를 해야함,,


def sol(start):
    global total,minval
    
    if total<minval:
        checklist[start]=1
 
        if 0 not in checklist:
            total+=field[start][0]
            if total<minval:
                minval=total
            total-=field[start][0]

        else:
            for i in range(N):
                if checklist[i]==0:
                    total+=field[start][i]
                    sol(i)
                    total-=field[start][i]
        checklist[start]=0
 
for tc in range(1,1+Testcase):
    N=int(input())

    checklist=[0]*N
    
    minval=100000
    total=0
    
    field=[list(map(int,input().split())) for _ in range(N)]
    
   
    sol(0)
    print('#{} {}'.format(tc,minval))
