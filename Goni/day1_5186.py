import sys
sys.stdin=open("sample_input.txt","r")

T=int(input())

for test_case in range(1,T+1):
    N=float(input())
    count=0
    num=N
    deci=N-int(N)
    ans=''

    for i in range(13):
        num*=2
        count+=1
        ans+=str(int(num))
        if num>1:
            num-=1
            if num==deci:
                print("#", test_case, sep='', end=' ')
                print(ans)
                break
        if num==1:
            print("#", test_case, sep='', end=' ')
            print(ans)
            break

    if count==13:
        print("#", test_case, sep='', end=' ')
        print("overflow")


