n=int(input())
ans=0
ch=[0]*n
diag1=[] # 오른쪽 아래로 향하는 대각선
diag2=[] # 왼쪽 아래로 향하는 대각선

def check(cnt, j, n) : # 대각선에 퀸이 배치되었는지를 체크하는 함수
    if((cnt+j in diag1) or ((cnt-j+n-1) in diag2)) :
        return False
    else :
        return True


def chess(cnt) :
    global ans
    if(cnt==n) : # cnt=n-1일 때 검사를 통해 넘어온 것이므로
        ans+=1 # 여기서는 ans의 값만 올려주고 리턴
        return
    for j in range(n) :
        if(ch[j]==0 and check(cnt, j, n)==True) : # 같은 열이나 대각선에 퀸이 없다면
            ch[j]=1 # 퀸 배치
            diag1.append(cnt+j)
            diag2.append(cnt-j+n-1)
            chess(cnt+1) # 재귀함수
            diag1.pop() # 맨 오른쪽에 요소가 추가된 것이므로 pop
            diag2.pop()
            ch[j]=0 # 0~(n-1)까지의 열을 돌아야 하므로 다시 빼줌

for i in range(n) :
    ch[i]=1
    diag1.append(i) # 초기 위치에서의 대각선
    diag2.append(n-i-1)
    chess(1) # 0번째 행애는 이미 퀸이 배치되었으므로 1부터 시작
    ch[i]=0
    diag1.pop()
    diag2.pop()

print(ans)

# 참고용 값
# queen=[0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
