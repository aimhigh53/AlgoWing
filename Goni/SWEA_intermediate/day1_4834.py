import sys
sys.stdin=open("sample_input.txt",'r')
T=int(input())

for test_case in range(1,T+1):
    N=int(input())
    temp=input()
    nums=[]
    for i in temp:
        nums.append(int(i))
    keys=[i for i in range(0,10)]
    count_dic=dict.fromkeys(keys,0)

    for num in nums:
        count_dic[num]+=1

    max=0
    for i in keys:
        if max<=count_dic[i]:
            max=count_dic[i]
            key=i
    print("#{} {} {}".format(test_case,key,max))


#카운트 안쓰고 해보고 싶었음,,딕셔너리 이용도 할겸,,
