t=int(input())

def bt(n, cnt, ch) : #ch는 체크리스트, cnt는 행을 카운트하기 위한 변수
    global ans, msum # msum은 중간합
    if(msum>=ans) : # 합이 크거나 같을 경우 탐색 중지
        return
    if(cnt==n) : # cnt가 n까지 도달한 겨우
        if(ans>msum) : # ans에 더 큰 값이 저장되어 있다면
            ans=msum # ans의 값을 바꿔줌
        return
    for j in range(n) :
        if(ch[j]==0) : # 열이 겹치지 않는다면
            ch[j]=1
            msum+=a[cnt][j] # 합을 늘려 줌
            bt(n, cnt+1, ch) # 재귀함수
            ch[j]=0
            msum-=a[cnt][j] # 0~(n-1)까지의 열을 돌아야 하므로 다시 빼줌

for tc in range(t) :
    n=int(input())
    a=[]
    ans=10**5 # 초기값을 크게 잡아줌
    ch=[0]*n

    for i in range(n) :
        a.append(list(map(int, input().split())))

    for i in range(n) :
        msum=a[0][i]
        ch[i]=1
        bt(n, 1, ch) # msum의 초기값을 a[0][i]로 잡았기 때문에 cnt는 1부터 시작
        ch[i]=0 # 탐색의 진행을 위해 ch[i]=0으로 재설정
    print('#%d'%(tc+1), ans)
