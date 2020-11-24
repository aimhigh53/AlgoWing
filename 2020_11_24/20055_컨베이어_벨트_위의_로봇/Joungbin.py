from collections import deque

n, k = map(int, input().split())
m = 2*n

belt = [*map(int, input().split())] # Durability of Conveyer Belt
rob = [0] * m
belt = deque(belt)
rob = deque(rob)
phase = 0

while True :
    phase += 1
    belt.appendleft(belt.pop()) # 1단계
    rob.appendleft(0)
    rob.pop()
    if(rob[n - 1] == 1) : rob[n - 1] = 0 # 맨 오른쪽에 있는 로봇 내림
    for i in range(n-2, -1, -1):
        if(rob[i] == 1 and rob[i + 1] == 0 and belt[i + 1] >= 1): # 2단계
            rob[i + 1] = 1
            rob[i] = 0
            belt[i + 1] -= 1
    if(rob[n - 1] == 1) : rob[n - 1] = 0
    if(rob[0] == 0 and belt[0] >= 1): rob[0] = 1; belt[0] -= 1 # 3단계
    if(belt.count(0) >= k): break # 4단계

print(phase)
