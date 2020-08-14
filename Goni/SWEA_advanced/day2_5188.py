import sys
sys.stdin=open("sample_input.txt","r")


T=int(input())
for test_case in range(1,T+1):
    size=int(input())
    box=[]
    cost=[[0]*size for _ in range(size)]

    for i in range(size):
        box.append(list(map(int,input().split())))

    for x in range(size-1,-1,-1):
        for y in range(size-1,-1,-1):
            if x==size-1 and y==size-1:
                cost[x][y] = box[x][y]
            else:
                if x+1==size:
                    cost[x][y] = cost[x][y + 1] + box[x][y]
                elif y+1==size:
                    cost[x][y] = cost[x + 1][y] + box[x][y]

                else:
                    cost[x][y] = min(cost[x][y + 1] + box[x][y], cost[x + 1][y] + box[x][y])

    print("#", test_case, sep='', end=' ')
    print(cost[0][0])
