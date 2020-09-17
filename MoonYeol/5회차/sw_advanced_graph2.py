def getParent(parent,node):
    if parent[node] == node:
        return node;
    return getParent(parent,parent[node])

def union(parent, x, y):
    x = getParent(parent,x)
    y = getParent(parent,y)
    #작은 수를 부모로 삼음
    if x <y:
        parent[y] = x
        return x
    else:
        parent[x] = y
        return y

def findParent(parent, x,y):
    x = getParent(parent,x)
    y = getParent(parent,y)
    if x == y:
        return True
    else:
        return False



num = int(input())
numbers = []
Ns = []
for i in range(num):
    N,M = map(int,input().split())
    Ns.append(N)
    temp = list(map(int, input().split()))
    temp2 = []
    j =0
    while j < len(temp):
        temp2.append([temp[j], temp[j+1]])
        j +=2
    numbers.append(temp2)



for idx, i in enumerate(numbers):
    answer = -1
    parent = [i for i in range(Ns[idx]+1)]
    for j in i:
        if not findParent(parent,j[0],j[1]):
            union(parent,j[0],j[1])
    for index ,j in enumerate(parent):
        if parent[index] == index:
            answer +=1
    print("#" + str(idx+1) +" " + str(answer))

