#아이디어 얻으려고 검색했는데,,,,블로그 코드 한번 보고 나니 그 외 생각이 안나서 그대로 구현
#원래는 stack으로 했으나 시간초과,,
#정신건강을 위해 바로 블로그대로 deque로 바꿈...
#출처 https://hongsj36.github.io/2020/02/01/Ad_GraphBasic/

import sys

from collections import deque

sys.stdin=open("sample_input.txt",'r')
def four_case(now_num,now_count, i):
    now_count+=1
    if i==0:
        now_num+=1
        if bound(now_num):
            Q.append((now_num,now_count))
            checks[now_num]=1
    elif i==1:
        now_num-=1
        if bound(now_num):
            Q.append((now_num,now_count))
            checks[now_num] = 1
    elif i==2:
        now_num*=2
        if bound(now_num):
            Q.append((now_num,now_count))
            checks[now_num] = 1
    else:
        now_num-=10
        if bound(now_num):
            Q.append((now_num,now_count))
            checks[now_num] = 1

def nogada():
    while(Q):
        num,count=Q.popleft()
        if num==to_num:
            return count
        else:
            for i in range(0,4):
                four_case(num,count,i)

def bound(num):
    if 0<num<=1000000 and checks[num]!=1:
        return True

T=int(input())

for test_case in range(1,T+1):
    from_num,to_num=map(int,input().split())
    global Q
    Q=deque()
    Q .append((from_num,0))
    global checks
    checks=[0]*1000001
    checks[from_num]=1

    print("#{} {}".format(test_case,nogada()))