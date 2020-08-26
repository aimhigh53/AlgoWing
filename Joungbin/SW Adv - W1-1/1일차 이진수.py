t=int(input())
bi=['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

for tc in range(t) :
    n, m=map(str, input().split())
    print('#%d'%(tc+1), end=' ')
    for i in m :
        print(bi[int(i, 16)], end='')
    print()