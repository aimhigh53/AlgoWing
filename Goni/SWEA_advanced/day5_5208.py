import sys
sys.stdin=open("sample_input.txt","r")

def backtracking():
    k=1
    while(0<k and k<len(vector)):
        getnext(k)
        if vector[k]==-1 :
            k-=1
        elif min(ans) <= vector.count(1):
            vector[k]=-1
            k -= 1
        else:
            if flag==1:
                ans.append(vector.count(1))

            else:
                k+=1

def getnext(k):
    global flag
    if vector[k]==-1:
        i=0
    elif flag==1 or vector[k]==1:
        vector[k]=-1
        flag=0
        return
    else:
        i=1

    while(i<len(candi)):

        vector[k]=candi[i]
        if Bound(k):
            return
        i+=1

    vector[k]=-1


def Bound(k):
    global flag
    temp=list(reversed(vector))
    a = temp.index(1)
    a = len(vector)-1 - a

    if a+battery[a]>=N-1 :
        flag=1
        return True

    elif vector[k]==0 and a+battery[a]==k:
        return False

    return True


T=int(input())
for test_case in range(1,T+1):
    flag=0
    temp=list(map(int,input().split()))
    N=temp[0]
    battery=temp[1:]
    vector = [-1] * (N-1)
    vector[0] = 1
    candi = [0, 1]
    ans=[99999999]
    backtracking()


    print("#",test_case,sep='',end=' ')

    print(min(ans)-1)