## 5248_그룹 나누기
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
# https://hongsj36.github.io/2020/02/01/Ad_GraphBasic/ 참고했습니다

# 부모 노드 찾기
def find_set(x) :
    if parent[x] == x :
        return x
    else :
        return find_set(parent[x])

# 합집합 만들기
def union(x, y) :
    x = find_set(x)
    y = find_set(y)
    if rank[x] >= rank[y] :
        parent[y] = x
        if rank[x] == rank[y] :
            rank[x] += 1
    else :
        parent[x] = y

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    paper = list(map(int, input().split()))
    parent = [i for i in range(N+1)] # 자리 맞추기 위해 0번째도 넣음
    rank = [0] * (N + 1) # 자리 맞추기 위해 0번째도 넣음

    for i in range(M) : # 두개 씩 묶기
        union(paper[2 * i], paper[2 * i + 1])
        
    groups = set() # 부모 노드만 모으기 & 중복 제거
    for j in range(1, N+1) :
        groups.add(find_set(j))
    print('#' + str(test_case), len(groups))
