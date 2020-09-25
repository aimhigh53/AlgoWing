import sys
sys.stdin=open("sample_input.txt",'r')

T=int(input())

for test_case in range(1,T+1):
    node_num=int(input())
    nums=list(map(int,input().split()))
    tree=[-1]*(node_num+1)

    assignTree=0

    for num in nums:
        assignTree+=1
        tree[assignTree]=num
        toChangePosition=assignTree

        while toChangePosition//2>=1:
            if tree[toChangePosition] < tree[toChangePosition // 2]:
                temp=tree[toChangePosition]
                tree[toChangePosition]=tree[toChangePosition // 2]
                tree[toChangePosition // 2]=temp
            toChangePosition//=2

    ans=0
    toCheckParent=node_num
    while(toCheckParent > 1):
        toCheckParent //= 2
        ans+=tree[toCheckParent]

    print("#{} {}".format(test_case, ans))

