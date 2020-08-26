import sys
sys.stdin=open("sample_input.txt",'r')
T=int(input())

for test_case in range(1,T+1):
    N=int(input())
    lst=list(map(int,input().split()))

    print("#", test_case, sep='', end=' ')
    print(max(lst)-min(lst))

