from itertools import permutations

t=int(input())

for tc in range(t) :
    n=int(input())
    a=[]
    ans=0
    for i in range(n) :
        a.append(list(map(int, input().split())))
    l=[*range(1, n)]
    print(l)
    b=list(permutations(l, n-1))
    print(b)
    for i in range(len(b)) :
        s=0
        s+=a[0][b[i][0]]
        #print(s, end=' ')
        for j in range(1, n-1) :
            s+=a[b[i][j-1]][b[i][j]]
            #print(s, end=' ')
        s+=a[b[i][n-2]][0]
        #print(s, end=' ')
        if(ans==0 or s<ans) :
            ans=s
        #print('%d :'%(i+1), s)
    print(ans)