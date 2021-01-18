'''
완전 하드코딩에 조합도 구현 안함 꼭 다시 해보기!
'''
from itertools import combinations
l,c=map(int,input().split())
nums=[i for i in range (c)]
clist=list(input().split())
clist.sort()
vowel=['a','e','i','o','u']
consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
target=list(combinations(nums,l))

for each in target:
    temp=[]
    flag1=False
    flag2=False
    count=0
    for i in range(l):
        temp.append(clist[each[i]])
    for j in vowel:
        if j in temp:
            flag1=True
    for j in consonants:
        if j in temp:
            count+=1

            if count==2:
                flag2=True
                break
    if flag1 and flag2:
        for _ in temp:
            print(_,end='')
        print()
