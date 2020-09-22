


def solution(tree,N,idx):
    global count
    if idx <= N:
        solution(tree,N,idx*2)
        tree[idx] = count
        count += 1
        solution(tree,N,idx*2+1)

T = int(input())

Ns = []

for i in range(T):

    N = int(input())
    Ns.append(N)


for idx, N in enumerate(Ns):
    tree = [0 for i in range(N + 1)]
    count=1
    answer = solution(tree,N,1)
    print("#" + str(idx+1) +" " + str(tree[1]) + " " +str(tree[N//2]))
