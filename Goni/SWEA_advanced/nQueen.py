def backtraking():
    k=0
    ans=0
    while(0<=k and k<len(vector)):
        getnext(k)
        if vector[k]==-1:
            k-=1
        else:
            if k==N-1:
                ans+=1
            else:
                k+=1
    return ans

def getnext(k):
    i=vector[k]
    while(i<N-1):
        i += 1
        vector[k]=i
        if Bound(k):
            return
    vector[k]=-1

def Bound(k):
    for i in range(0,k):
        if vector[k]==vector[i] or k-i==abs(vector[k]-vector[i]):
            return False
    return True


N=int(input())
vector=[-1]*N
backtraking()
print(backtraking())
