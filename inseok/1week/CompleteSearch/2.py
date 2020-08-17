def sol(i):
    global mini,tot
 
    if tot<mini:
        check[i]=1
 
        if 0 not in check:
            tot+=field[i][0]
            if tot<mini:
                mini=tot
            tot-=field[i][0]
        else:
 
            for j in range(N):
                if check[j]==0:
                    tot+=field[i][j]
                    sol(j)
                    tot-=field[i][j]
        check[i]=0
 
T=int(input())
for Tcase in range(1,1+T):
    N=int(input())
    mini=100000
    tot=0
 
    field=[list(map(int,input().split())) for _ in range(N)]
    check=[0]*N
 
    sol(0)
    print('#{} {}'.format(Tcase,mini))
    Tcase-=1
 
