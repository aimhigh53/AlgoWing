import heapq

t = int(input())

for tc in range(t):
    heap = []
    n = int(input())
    input_list = list(map(int, input().split()))
    for x in input_list:
        heapq.heappush(heap, x)
    heap.insert(0, 0)
    ans = 0
    index = len(heap) - 1
    while(index >= 1):
        index //= 2
        ans += heap[index]
    print('#%d' % (tc+1), ans)
