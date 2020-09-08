import sys
sys.stdin=open("sample_input.txt",'r')

T=int(input())

for test_case in range(1,T+1):
    A_num,B_num=map(int,input().split())
    A_words=[]
    B_words=[]
    count=0

    for _ in range(A_num):
        A_words.append(input())
    for _ in range(B_num):
        B_words.append(input())

    for A_each in A_words:
        if A_each in B_words:
            count+=1

    print("#{} {}".format(test_case,count))
