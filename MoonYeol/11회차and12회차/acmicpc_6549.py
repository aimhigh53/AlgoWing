import sys

sys.setrecursionlimit(10**6)
INF = float('inf')
class SegmentTree():
    def __init__(self, m):
        self.max_value = 0
        n = 1
        while n < m:
            n *= 2

        self.tree = [[INF, INF] for i in range(n * 2)]
        self.m = m  # 리프노드 개수
        self.n = n

    def insert(self, arr):
        #print(arr)
        for i in range(self.n, self.n + len(arr)):
            self.tree[i][0] = arr[i - self.n]
            self.tree[i][1] = i - self.n +1
        for i in range(self.n - 1, 0, -1):
            if self.tree[i * 2][0] > self.tree[i * 2 + 1][0]:
                self.tree[i] =self.tree[i * 2 + 1]
            else:
                self.tree[i] = self.tree[i * 2]
        self.max_value = max(arr)

    def getMin(self, left, right):
        l = left + self.n - 1
        r = right + self.n - 1
        rval = INF
        ridx = 0
        while l <= r:

            if l % 2 == 0:
                l //= 2
            else:
                if rval >= self.tree[l][0]:
                    rval = self.tree[l][0]
                    ridx = self.tree[l][1]
                l = (l // 2) + 1
            if r % 2 == 1:
                r //= 2
            else:
                if rval >= self.tree[r][0]:
                    rval = self.tree[r][0]
                    ridx = self.tree[r][1]
                r = (r // 2) - 1

        return rval, ridx





def solution(histogram,left,right):
    if left >= right:
        return histogram.getMin(right,left)[0]
    if right - left + 1 <= 2 :
        return histogram.getMin(left,right)[0]*(right-left+1)
    ans = 0
    min_value, min_idx = histogram.getMin(left,right)
    left_part = 0
    right_part = 0
    if min_idx -1 >= left:
        left_part = solution(histogram, left, min_idx-1)
    if min_idx +1 <= right:
        right_part = solution(histogram, min_idx+1, right)
    ans = max(min_value*(right-left+1), left_part, right_part)
    return ans


testCases = []
line = input()
while line != '0':

    temp = list(map(int,line.split()))
    seg = SegmentTree(temp[0])
    seg.insert(temp[1:])
    testCases.append(seg)
    line = input()

for testCase in testCases:
    print(max(testCase.max_value,solution(testCase,1,testCase.m)))