t = int(input())

for tc in range(t):
    n, m = map(int, input().split()) # 컨테이너 수, 트럭 수
    container = list(map(int, input().split()))
    container.sort()
    truck_cap = list(map(int, input().split()))
    truck_cap.sort()
    ans = 0
    for i in range(min(n, m)):
        if(container[len(container) - 1]<=truck_cap[len(truck_cap) - 1]) :
            ans += container[len(container) - 1]
            truck_cap.pop()
        container.pop()
    print('#%d'%(tc+1), ans)
