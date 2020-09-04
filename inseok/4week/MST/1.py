testcase=int(input())

def findset(x):
    if x==parent[x]:
        return x
    else:
        return findset(parent[x])

def union(x,y):
    parent[findset(y)]=findset(x)

# def makeset(x):
#     p[x]=x
#     rank[x]=0
    
    
    
for tc in range(1,1+testcase):
    V,E=map(int,input().split(' '))
#     mst=[]

    #makeset
    parent = [i for i in range(V+1)]
    edge = [list(map(int, input().split())) for _ in range(E)]
  
    edge.sort(key=lambda t:-t[2])
    cost=0
    
    while edge:
        u,v,val=edge.pop()
        if findset(u)!=findset(v):
            union(u,v)
#             mst.append((u,v))
            cost+=val    
    print('#{} {}'.format(tc,cost))
    
    
    
