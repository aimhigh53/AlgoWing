class MinHeap():
    def __init__(self):
        self.heap = [0]

    def insert(self, value):
        # 맨 마지막 위치에 원소를 임시로 삽입.
        self.heap.append(value)
        now = self.getLast()
        # 부모를 타고 올라가면서 크기를 비교
        while 0 < now:
            parent = self.getParent(now)
            if 0 < parent and self.heap[parent] > self.heap[now]:
                self.swap(now, parent)
                now = parent
            else:
                break

#마지막 노드를 루트노드랑 자리를 바꾸고 마지막 노드 pop
#heap 재정렬하는 식으로 삭제
    def delete(self):
        lastIndex = self.getLast()
        if lastIndex <= 0:
            return -1
        self.swap(1, lastIndex)
        temp = self.heap.pop()
        self.heapify(1)
        return temp

#힙 재정렬 함수
    def heapify(self, idx):
        # idx에서 부터 자식노드로 내려가면서 heap 조건 충족 시키게 정렬
        left = self.leftchild(idx)
        right = self.rightchild(idx)
        minIndex = idx

#자식중에 자신보다 더 작은 값이 있다면 재귀적으로 heapify 시킴
        if left < len(self.heap) and self.heap[minIndex] > self.heap[left]:
            minIndex = left
        if right < len(self.heap) and self.heap[minIndex] > self.heap[right]:
            minIndex = right

        if minIndex != i:
            self.swap(i, minIndex)
            self.heapify(minIndex)

    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

#왼쪽 자식의 index구하는 함수
    def getLeft(self, idx):
        return idx * 2

#오른쪽 자식의 index 구하는 함수
    def getRight(self, idx):
        return idx * 2 + 1

#부모 노드의 index 구하는 함수
    def getParent(self, index):
        return index // 2

#마지막 원소의 index 구하는 함수
    def getLast(self):
        return len(self.heap) - 1

    def solution(self, now):
        if now <= 0:
            return 0
        return self.heap[now] + self.solution(self.getParent(now))


T = int(input())

testCases = []

for i in range(T):
    N = int(input())
    testCases.append(list(map(int, input().split())))

for idx, values in enumerate(testCases):
    heap = MinHeap()
    for i in values:
        heap.insert(i)

    print("#" + str(idx + 1) + " " + str(heap.solution(heap.getParent(heap.getLast()))))
