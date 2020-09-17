def solution(child,N):
    count = 1
    for i in child[N]:
        count += solution(child,i)
    return count

T = int(input())
testcases = []
Es = []
Ns = []

for i in range(T):
    E, N = map(int,input().split())
    childs = [[] for i in range(E+2)]
    Ns.append(N)
    temp = list(map(int,input().split()))
    for j in range(0, E*2, 2):
        childs[temp[j]].append(temp[j+1])
    testcases.append(childs)


for idx, testcase in enumerate(testcases):
    answer = solution(testcase,Ns[idx])
    print("#" + str(idx+1) +" " + str(answer))
