import sys
sys.stdin=open("sample_input.txt",'r')

T=int(input())

for test_case in range(1,1+T):
    N=int(input())
    box = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        a,b,c,d,color=map(int,input().split())
        for left in range(a,c+1):
            for right in range(b,d+1):
                box[left][right]+=color


    count=0
    for i in range (10):
        for j in range(10):
            if box[i][j]==3:
                count+=1

    print("#{} {}".format(test_case,count))
