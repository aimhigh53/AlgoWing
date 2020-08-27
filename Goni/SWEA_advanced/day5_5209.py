import sys
sys.stdin=open("sample_input.txt",'r')
def backtraking():
    k=0
    while(0<=k and k<len(vector)):
        getnext(k)
        if vector[k]==-1:
            k-=1
        else:
            if k==N-1:
                ans.append(candi)

            else:
                k+=1


def getnext(k):

    i=vector[k]
    while(i<N-1):
        i += 1
        vector[k]=i
        if Bound():
            return

    vector[k]=-1

def Bound():
    global candi
    breaker=False
    candi=0
    for i in range(len(vector)):
        for k in range(i+1,len(vector)):
            if vector[i]!=-1:
                if vector[i]==vector[k]:
                    return False
            elif vector[i]==-1:
                breaker=True
                break
        if breaker:
            break

    k=0
    for i in vector:
        if i!=-1:
            candi+=box[k][i]
            k+=1
    if min(ans)>candi:
        return True
    else:
        return False



T=int(input())

for test_case in range(1,T+1):
    global ans
    ans=[0]
    N=int(input())
    box=[]
    for _ in range(N):
        temp=list(map(int,input().split()))
        box.append(temp)
    vector=[-1]*N
    for i in box:
        ans[0]+=i[0]
    backtraking()

    print("#", test_case, sep='', end=' ')
    print(min(ans))