#N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오

from collections import deque

Testcase=int(input())

#A,B,C,D,E,F,10,11,12,13,14,15
#{1,1,1,1},{1,1,1,0},{1,1,0,1},{1,1,0,0},{1,0,1,1},{1,0,1,0}

def sol(dq):
    anslist=[]
    while dq:

        onechar=dq.popleft()
        asci=ord(onechar)
        if not 65<=asci<=70:
            onechar=int(onechar)
            tmp="{0:b}".format(onechar).zfill(4)
            anslist.append(tmp)
        else:
            if asci==65:
                anslist.append("1010")
            elif asci==66:
                anslist.append("1011")
            elif asci==67:
                anslist.append("1100")
            elif asci==68:
                anslist.append("1101")
            elif asci==69:
                anslist.append("1110")
            else:
                anslist.append("1111")

    ansstr=''.join(anslist)
    return ansstr
            
        
for tc in range(1,1+Testcase):
    N,hexatobin=map(str,input().split(' '))
    dq=deque(list(hexatobin))
    ansstr=sol(dq)
    
    
    print("#{} {}".format(tc,ansstr))

