import sys
sys.stdin=open("sample_input.txt",'r')

T=int(input())

for test_case in range(1,T+1):
    node_num,leaf_num,toCheck=map(int,input().split())
    tree=[-1]*(node_num+1)

    for _ in range(leaf_num):
        node,num=map(int,input().split())
        tree[node]=num

    temp=1
    while(temp<=node_num):
        temp*=2
    now=temp//2
    left=now

    while(left>=1):
        while(now+1<=now*2-1 and now+1<=node_num):
            tree[now//2]=tree[now]+tree[now+1]
            now+=2
        if now==node_num:
            tree[now//2]=tree[now]
        left//=2
        now=left
    print("#{} {}".format(test_case,tree[toCheck]))

