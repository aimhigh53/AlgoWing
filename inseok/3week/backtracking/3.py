
#파이썬 시간초과,,,,pypy3성공
def promising(i):
    for k in range(i):
        #대각선, 같은행처리 
        if abs(field[i]-field[k])==i-k or field[k]==field[i]:
            return False   
    return True       

def sol(i):
    global cnt

    if N==i:
        cnt+=1
    else:
        
        for s in range(N):
            field[i]=s
            if promising(i):
                sol(i+1)


N=int(input())
field=[0]*15
cnt=0
sol(0)
print(cnt)
