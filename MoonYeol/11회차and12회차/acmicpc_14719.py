INF = float('inf')
class SegmentTree():
    def __init__(self, m):
        n = 1
        while n < m:
            n *= 2

        self.tree = [INF for i in range(n * 2)]
        self.m = m  # 리프노드 개수
        self.n = n

    def insert(self, arr):
        for i in range(self.n, self.n + len(arr)):
            self.tree[i] = arr[i - self.n]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])

    def getMax(self, left, right):
        l = left + self.n - 1
        r = right + self.n - 1
        rval = 0
        while l <= r:

            if l % 2 == 0:
                l //= 2
            else:
                rval = max(rval,self.tree[l])
                l = (l // 2) + 1
            if r % 2 == 1:
                r //= 2
            else:
                rval = max(rval,self.tree[r])
                r = (r // 2) - 1

        return rval


def solution(seg,blocks):
    answer = 0
    left = 1
    right =seg.m
    for i in range(1,len(blocks)+1):
        left_max = seg.getMax(left,i)
        right_max = seg.getMax(i,right)
        low = min(left_max,right_max)
        answer += low - blocks[i-1]
    return answer




H, W = map(int, input().split())
seg = SegmentTree(W)
blocks =list(map(int, input().split()))
seg.insert(blocks)

print(solution(seg,blocks))