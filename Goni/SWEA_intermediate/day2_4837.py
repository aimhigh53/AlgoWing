import sys
sys.stdin=open("sample_input.txt",'r')

import itertools

T = int(input())
A=[i for i in range(1,13)]

for test_case in range(1, T+1):
    sub, total=map(int,input().split())
    subsets=list(map(set,itertools.combinations(A, sub)))
    count=0
    for k in range(len(subsets)):
        if sum(subsets[k])==total:
            count+=1
    print("#", test_case, sep='', end=' ')
    print(count)

