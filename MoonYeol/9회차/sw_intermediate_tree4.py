class SegmentTree():
    def __init__(self,n,m):
        self.tree = [0 for i in range(n+1)] # 트리는 n+1 길이, index 0은 사용하지 않는다
        self.m = m #리프노드 갯수
        self.n = n #트리노드 갯수

    def insert(self, idx, value):
        #tree의 idx의 위치에 value값 삾입
        self.tree[idx] = value

    def calcSegment(self):
        #세그먼트 트리의 구간 정보를 계산한다
        for i in range(self.n -self.m ,0 ,-1):
            #왼쪽 오른쪽 자식 둘다 존재 할경우
            if i*2 <= self.n and i*2 +1 <= self.n:
                self.tree[i] = self.tree[i*2] + self.tree[i*2 +1]
            #왼쪽 자식만 존재할 경우
            elif i*2 <= self.n:
                self.tree[i] = self.tree[i*2]
            #자식 둘 다 없는 경우는 존재할 수 없다.


    def getSum(self,idx):
        #구간 정보를 반환
        return self.tree[idx]


T = int(input())

testCases = []

for i in range(T):
    N,M,L = map(int,input().split())
    seg = SegmentTree(N,M)
    for j in range(M):
        idx, value = map(int,input().split())
        seg.insert(idx,value)

    seg.calcSegment()

    print("#" + str(i + 1) + " " + str(seg.getSum(L)))
