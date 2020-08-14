import sys
sys.stdin=open("sample_input.txt","r")

T=int(input())
Alphabet={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,}
for test_case in range(1,T+1):
    N,hexa=input().split()
    print('#{}'.format(test_case),end=' ')
    for i in hexa:
        ans = []
        if i.isdigit():
            temp=int(i)
        else:
            temp=Alphabet[i]

        for j in range(4):
            if temp & (1 << j):
                ans.append(1)
            else:
                ans.append(0)
        ans.reverse()
        for k in ans:
            print(k,end='')
    print()

