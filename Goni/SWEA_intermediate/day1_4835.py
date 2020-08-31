import sys
sys.stdin=open("sample_input.txt","r")

T=int(input())

for test_case in range(1,T+1):
    num,section=map(int,input().split())

    nums=list(map(int,input().split()))
    plus=[0]*(num-section+1)
    for first in range(0,num-section+1):
        for count in range(0,section):
            plus[first]+=nums[first+count]
    print('#{} {}'.format(test_case,max(plus)-min(plus)))