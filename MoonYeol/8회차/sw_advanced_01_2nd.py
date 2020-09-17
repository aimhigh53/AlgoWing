'''
16진수 1자리는 2진수 4자리로 표시된다.

N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.

단, 2진수의 앞자리 0도 반드시 출력한다.

예를 들어 47FE라는 16진수를 2진수로 표시하면 다음과 같다.

0100011111111110


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 자리 수 N과 N자리 16진수가 주어진다. 1<=N<=100

16진수 A부터 F는 대문자로 표시된다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력

3
4 47FE
5 79E12
8 41DA16CD

출력
#1 0100011111111110
#2 01111001111000010010
#3 01000001110110100001011011001101
'''

alphabet={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}

#나머지 연산을 통해 2진수 계산, zfill함수 통해 4자리로 채움
def getBinary(num):
    ans = ''
    while num>0:
        ans = str(num%2) + ans
        num //= 2
    return ans.zfill(4)

#16진수를 숫자로 바꿈, 한 자리 씩 getBinary함수 호출
def solution(hexa):
    ans = ''
    for i in hexa:
        if i.isdigit():
            num = int(i)
        else:
            num = alphabet[i]
        ans += getBinary(num)
    return ans

#main
if __name__ == "__main__":
    num = int(input())
    ns = []
    hexs = []
    #입력
    for i in range(num):
        n, hexa  = input().split()
        hexs.append(hexa)
    #출력 및 solution호출
    for idx, value in enumerate(hexs):
        print("#" + str(idx+1) + " " + solution(value))
