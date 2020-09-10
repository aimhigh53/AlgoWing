#한문제 런타임에러
import sys
sys.stdin=open("sample_input.txt",'r')

T=int(input())

for test_case in range(1,T+1):
    N,text=input().split()
    N=int(N)
    count=0
    candi=[]

    for start in range(len(text)):
        for length in range(1,len(text)-start+1):
            candi.append(text[start:start+length])
    candi=sorted(set(candi))

    print("#{} {} {}".format(test_case,candi[N-1][0],len(candi[N-1])))