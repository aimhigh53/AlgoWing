import sys
sys.stdin=open("sample_input.txt",'r')

T=int(input())

for test_case in range(1,T+1):
    pairNum,target=map(int,input().split())
    pairs=list(map(int,input().split()))
    pairDict={}
    stack=[target]
    visited=[target]
    ans=1

    for index in range(0,pairNum*2,2):
        parent=pairs[index]
        if parent in pairDict:
            pairDict[parent]=[pairDict[parent][0],pairs[index+1]]
        else:
            pairDict[parent]=[pairs[index + 1]]

    while(stack):
        target=stack.pop()
        if target in pairDict:
            for candi in pairDict[target]:
                if candi not in visited:
                    visited.append(candi)
                    stack.append(candi)
                    ans+=1

    print("#{} {}".format(test_case,ans))

