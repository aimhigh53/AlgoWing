import sys
sys.stdin=open("sample_input.txt",'r')

T=int(input())

for test_case in range(1,T+1):
    wordsNum,prefixNum=map(int,input().split())
    words=[]
    prefixCandi=[]
    count=0
    for _ in range(wordsNum):
        words.append(input())
    for _ in range(prefixNum):
        prefixCandi.append(input())

    for each_prefixCandi in prefixCandi:
        lenOfCandi=len(each_prefixCandi)
        for word in words:
            if word[:lenOfCandi]==each_prefixCandi:
                count+=1
                break


    print("#{} {}".format(test_case,count))
