import sys
sys.stdin=open("sample_input.txt",'r')

def baseToBinary(base):
    global ans
    temp=''
    for i in range(3,-1,-1):
        if base & 1<<i:
            temp+="1"
        else:
            temp+="0"
    ans+=temp

T=int(input())
alphabet={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}

for test_case in range(1,T+1):
    num,hexa=input().split()
    ans = ''
    for each in hexa:
        if each.isdigit():
            base=int(each)
            baseToBinary(base)
        else:
            base=alphabet[each]
            baseToBinary(base)

    print("#{} {}".format(test_case,ans))
